from django.urls import path
from .views import *
urlpatterns = [
    path("", index, name="home"),
    path("<str:link_slug>/", root_link, name="root-link"),
    path("link/create/", add_link, name="root-link"),
]
