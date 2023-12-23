from django.urls import path
from django_fullstack.views import welcome_page

urlpatterns = [path("", welcome_page, name="welcome")]