from django.urls import path
from . import views
from django.views.static import serve 

urlpatterns = [
    path("", views.home, name="home"),
    path("allgenre", views.genres, name="genres"),
    path('movies', views.movies, name="movies"),
    path('tvseries', views.tvseries, name="tvseries"),
    path('most-watched', views.mostwatched, name="mostwatched"),
    path('comingsoon', views.comingsoon, name="comingsoon"),
    path("<search>", views.search, name="search"),
]
