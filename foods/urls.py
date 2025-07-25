from django.urls import path

from foods.views import IndexView,MenuView,BookView,AboutView

urlpatterns=[
    path("", IndexView.as_view(), name="index"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("book/", BookView.as_view(), name="book"),
    path("about/", AboutView.as_view(), name="about"),
]