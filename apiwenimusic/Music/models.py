from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, null=False, unique=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    nameUser = models.CharField(max_length=200, blank=False, null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Music(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    artista = models.CharField(max_length=100, blank=False, null=False)
    playlist = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
