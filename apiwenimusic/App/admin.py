from django.contrib import admin
from App import models

# Register your models here.

admin.site.register(models.Music)
admin.site.register(models.Artista)
admin.site.register(models.Playlist)