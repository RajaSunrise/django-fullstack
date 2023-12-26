from django.apps import AppConfig
from django.core import checks

<<<<<<< HEAD
from django_vite.core.asset_loader import DjangoViteAssetLoader
=======
from django_fullstack.django_vite.core.asset_loader import DjangoViteAssetLoader
>>>>>>> a784bf9 (two commit)


class DjangoViteAppConfig(AppConfig):
    name = "django_vite"
    verbose_name = "Django Vite"

    def ready(self) -> None:
<<<<<<< HEAD
=======
        # Make Loader instance at startup to prevent threading problems
        # but do not crash while doing so.
>>>>>>> a784bf9 (two commit)
        DjangoViteAssetLoader.instance()

        # Check for potential errors with loading manifests in DjangoViteConfigs.
        checks.register(check_loader_instance, checks.Tags.staticfiles)


def check_loader_instance(**kwargs):
    return DjangoViteAssetLoader.instance().check(**kwargs)
