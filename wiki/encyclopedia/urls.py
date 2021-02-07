from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki_page, name="wiki_page"),
    path("wiki/<str:title>", views.search_page, name="search_page"),
]
