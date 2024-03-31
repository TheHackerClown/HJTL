from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("user", views.dash, name="dash"),
    path('error', views.error, name='error'),
    path('exit',views.exit,name='exit'),
    path('paybay',views.pay, name='pay')
]
