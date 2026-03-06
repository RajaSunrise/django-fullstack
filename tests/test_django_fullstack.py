from django_fullstack import __version__


def test_version():
    assert __version__ == '0.5.0'

from django.conf import settings
from django.test import SimpleTestCase
import os

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
