from django.urls import path
from .views import welcome_page

urlpatterns = [path("", welcome_page, name="welcome")]
