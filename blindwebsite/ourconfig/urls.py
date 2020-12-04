from . import views
from django.urls import path

urlpatterns = [
    path("", views.ourconfig_index, name="ourconfig_index"),

   
]