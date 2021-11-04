from Music.models import Music
from rest_framework import serializers

class MusicSerializer(serializers.ModelSerializer):
    class Meta: #Obrigatório
        model = Music
        fields = ['titulo', 'artista', 'playlist', 'id']