from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),          # matches {% url 'index' %}
    path("techstack/", views.techstack, name="techstack"),
    path("contact/", views.contact, name="contact"),
]
