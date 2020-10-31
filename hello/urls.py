from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ronan", views.ronan, name="ronan"),
    path("brian", views.brian, name="brian")
]