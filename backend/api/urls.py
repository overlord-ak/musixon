from django.urls import path
from .views import Playlist

urlpatterns = [
    path("", Playlist.as_view(), name="playlist"),
]
