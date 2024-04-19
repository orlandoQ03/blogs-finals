from django.urls import path
from .import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("create/", views.blog_create, name="blog_create"),
]