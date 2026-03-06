from django_fullstack import __version__


def test_version():
    assert __version__ == '0.5.0'

from django.conf import settings
from django.test import SimpleTestCase, RequestFactory
from django.contrib.messages.storage.fallback import FallbackStorage
import os
from unittest.mock import patch, MagicMock

import importlib.util
spec = importlib.util.spec_from_file_location("create-app", os.path.join(os.path.dirname(os.path.dirname(__file__)), "django_fullstack", "core", "management", "commands", "create-app.py"))
create_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(create_app)
CreateAppCommand = create_app.CreateAppCommand
from django_fullstack.core.handlers.files import TemplateFilesHandler

class DjangoFullstackTests(SimpleTestCase):
    def test_settings_loaded(self):
        self.assertTrue(hasattr(settings, 'RENDER_URL_SSR') or 'URL_SSR' in getattr(settings, 'RENDER', {}))
        self.assertTrue(hasattr(settings, 'TEMPLATE_ASSETS_PATH'))

    def test_middleware_installed(self):
        self.assertIn('render.middleware.RenderMiddleware', settings.MIDDLEWARE)

    def test_templates_dirs(self):
        templates = settings.TEMPLATES[0]
        dirs = [str(d) for d in templates['DIRS']]
        self.assertTrue(any('src' in d for d in dirs))
        self.assertTrue(any('templates' in d for d in dirs))

    def test_staticfiles_dirs(self):
        dirs = [str(d) for d in settings.STATICFILES_DIRS]
        self.assertTrue(any('assets' in d for d in dirs))
        self.assertTrue(any('public' in d for d in dirs))

class TemplateFilesHandlerTests(SimpleTestCase):
    def setUp(self):
        self.handler = TemplateFilesHandler()

    def test_get_templates(self):
        templates = self.handler.get_templates()
        self.assertIn('react', templates)
        self.assertIn('react_typescript', templates)
        self.assertIn('vue', templates)
        self.assertIn('vue_typescript', templates)

    def test_get_template_dir(self):
        path = self.handler.get_template_dir('react')
        self.assertTrue(str(path).endswith('react'))

        path_ts = self.handler.get_template_dir('react_typescript')
        self.assertTrue(str(path_ts).endswith('react_typescript'))

    @patch('django_fullstack.core.handlers.files.copy_files')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.exists')
    def test_create_project_files(self, mock_exists, mock_getcwd, mock_listdir, mock_copy_files):
        mock_getcwd.return_value = '/fake/dest/dir'
        mock_listdir.return_value = ['package.json', 'src']
        mock_exists.return_value = False

        args = MagicMock()
        args.framework = 'react'
        args.typescript = False

        self.handler.create_project_files(args)

        mock_copy_files.assert_called_once()
        called_src, called_dest = mock_copy_files.call_args[0]
        self.assertTrue(str(called_src).endswith('react'))
        self.assertEqual(called_dest, '/fake/dest/dir')

    @patch('django_fullstack.core.handlers.files.copy_files')
    @patch('os.listdir')
    @patch('os.getcwd')
    @patch('os.path.exists')
    def test_create_project_files_typescript(self, mock_exists, mock_getcwd, mock_listdir, mock_copy_files):
        mock_getcwd.return_value = '/fake/dest/dir'
        mock_listdir.return_value = ['package.json', 'src']
        mock_exists.return_value = False

        args = MagicMock()
        args.framework = 'react'
        args.typescript = True

        self.handler.create_project_files(args)

        mock_copy_files.assert_called_once()
        called_src, called_dest = mock_copy_files.call_args[0]
        self.assertTrue(str(called_src).endswith('react_typescript'))
        self.assertEqual(called_dest, '/fake/dest/dir')

class CreateAppCommandTests(SimpleTestCase):
    @patch('django_fullstack.core.handlers.files.TemplateFilesHandler.create_project_files')
    def test_create_app_handle(self, mock_create_project_files):
        command = CreateAppCommand()
        args = MagicMock()
        command.handle(args)
        mock_create_project_files.assert_called_once_with(args)

spec_start = importlib.util.spec_from_file_location("startproject", os.path.join(os.path.dirname(os.path.dirname(__file__)), "django_fullstack", "core", "management", "commands", "startproject.py"))
startproject = importlib.util.module_from_spec(spec_start)
spec_start.loader.exec_module(startproject)
StartProjectCommand = startproject.StartProjectCommand

class StartProjectCommandTests(SimpleTestCase):
    @patch('django.core.management.execute_from_command_line')
    def test_startproject_handle(self, mock_execute):
        command = StartProjectCommand()
        args = MagicMock()
        args.command = 'startproject'
        args.project_args = ['myproject', '.']
        command.handle(args)
        mock_execute.assert_called_once_with(['django-admin', 'startproject', 'myproject', '.'])

from django_fullstack.middleware import inertia_share

class InertiaMiddlewareTests(SimpleTestCase):
    def test_inertia_share_middleware(self):
        factory = RequestFactory()
        request = factory.get('/')

        # Mock user and messages
        request.user = MagicMock()
        request.user.is_authenticated = True

        # Set up a fake messages storage
        request.session = {}
        setattr(request, '_messages', FallbackStorage(request))

        get_response_mock = MagicMock()
        get_response_mock.return_value = "response"

        middleware = inertia_share(get_response_mock)

        # We need to patch get_messages or run it
        response = middleware(request)
        self.assertEqual(response, "response")
        get_response_mock.assert_called_once_with(request)

        # Checking inertia shared props
        # In inertia-django, shared props are often on request.inertia
        # We'll just verify no exceptions occur for now and response is returned

from django_fullstack.views import welcome_page

class ViewsTests(SimpleTestCase):
    @patch('django_fullstack.views.render')
    def test_welcome_page(self, mock_render):
        factory = RequestFactory()
        request = factory.get('/')
        welcome_page(request)

        mock_render.assert_called_once()
        called_request, called_template, called_props = mock_render.call_args[0]
        self.assertEqual(called_request, request)
        self.assertEqual(called_template, "index")
        self.assertIn("packages", called_props)
        self.assertEqual(called_props["packages"], ["Django", "Inertia.js", "Vite.js"])
