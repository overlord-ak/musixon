from rest_framework import serializers

from .models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "creator",
            "songs",
            "created_at",
        )

        model = Playlist
