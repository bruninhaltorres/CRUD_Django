from App.models import Music, Artista, Playlist
from rest_framework import fields, serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['nameMusic', 'artista', 'id']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['namePlaylist', 'musicas', 'id']

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['name', 'id']
