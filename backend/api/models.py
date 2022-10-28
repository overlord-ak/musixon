from django.db import models
from django.conf import settings


class Artist(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.PositiveIntegerField()
    genre = models.CharField(null=True, blank=True, max_length=100)
    youtube_id = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    title = models.CharField(max_length=150)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
