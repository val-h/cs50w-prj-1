from collections import namedtuple
from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki_page, name="wiki_page"),
    path("search/", views.search_page, name="search_page"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("random_page/", views.random_page, name="random_page"),
]
