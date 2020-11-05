from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("ronan", views.ronan, name="ronan"),
    path("brian", views.brian, name="brian")
]