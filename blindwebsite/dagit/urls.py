from django.urls import path
from . import views

urlpatterns = [
    path("", views.dagit_index, name="dagit_index"),
    path("<int:pk>/", views.dagit_detail, name="dagit_detail"),
    path("<kategori>/", views.dagit_kategori, name="dagit_kategori"),
]