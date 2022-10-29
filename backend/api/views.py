from rest_framework import generics
from .models import Playlist
from .serializers import PlaylistSerializer


class Playlist(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
