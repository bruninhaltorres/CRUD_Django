from django.contrib.auth.models import User
from django.db import models

class Artista(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

class Music(models.Model):
    nameMusic = models.CharField(max_length=100, blank=False, null=False)
    artista = models.ForeignKey(Artista, null=True, on_delete=models.CASCADE, related_name = 'artista')

    def __str__(self):
        return self.nameMusic

class Playlist(models.Model):
    namePlaylist = models.CharField(max_length=100, blank=False, null=False, unique=True)
    musicas = models.ManyToManyField(Music, blank=True)

    def __str__(self):
        return self.namePlaylist