import importlib.metadata

try:
    __version__ = importlib.metadata.version("django-fullstack")
except importlib.metadata.PackageNotFoundError:
    # This case handles scenarios where the package might not be fully installed,
    # e.g., during development or if accessed outside an installed environment.
    __version__ = "unknown"

default_app_config = "django_fullstack.apps.DjangoFullstackConfig"
