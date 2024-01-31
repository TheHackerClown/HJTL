from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.dash, name="dash")
]
