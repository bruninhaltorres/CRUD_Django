from django.contrib.auth.models import User
from django.db import models

class Artista(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

# Remover a musica da playlist e adicionar

# PRODUCT_STATUS = [
#     ("1", "Sim"),
#     ("2", "Não")
# ]

class Music(models.Model):
    nameMusic = models.CharField(max_length=100, blank=False, null=False)
    artista = models.ForeignKey(Artista, null=True, on_delete=models.CASCADE, related_name = 'artista')

    def __str__(self):
        return self.nameMusic

class Playlist(models.Model):
    namePlaylist = models.CharField(max_length=100, blank=False, null=False, unique=True)
    musicas = models.ForeignKey(Music, null=True, on_delete=models.CASCADE, related_name = 'musicas')
    # status = models.CharField(max_length=1, choices=PRODUCT_STATUS, default="")

    def __str__(self):
        return self.namePlaylist