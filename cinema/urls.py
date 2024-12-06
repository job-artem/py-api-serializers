# write urls here
from os.path import pathsep

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, ActorViewSet, CinemaHallViewSet, MovieViewSet, MovieSessionViewSet

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema-halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie-sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
