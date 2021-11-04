from django.shortcuts import render
from rest_framework.serializers import Serializer
from Music.models import Music
from Music.serialializers import MusicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# Pegando as informações da API:
@api_view(['GET'])
def MusicList(request):
    music = Music.objects.all()
    serializer = MusicSerializer(music, many = True)
    return Response(serializer.data)

# Enviando informações:
@api_view(['POST'])
def MusicPost(request):
    serializer = MusicSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Inserindo por ID:
@api_view(['PUT'])
def MusicPut(request, pk):
    music = Music.objects.get(id = pk)
    serializer = MusicSerializer(music, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def MusicDelete(request, pk):
    music = Music.objects.get(id = pk)
    music.delete()
    return Response('apagado')