from django.apps import AppConfig
from django_fullstack.settings import initialize

class DjangoFullstackConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_fullstack"

    def ready(self):
        initialize()
        from django_fullstack import urls
        from django.conf import settings
        from importlib import import_module
        root_urlconf = import_module(settings.ROOT_URLCONF)
        urlpatterns = getattr(root_urlconf, "urlpatterns", [])

        urlpatterns += urls.urlpatterns

        root_urlconf.urlpatterns = urlpatterns