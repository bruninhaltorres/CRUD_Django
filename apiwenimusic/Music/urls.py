from django.urls import path
from Music import views

urlpatterns = [
    path('getMusica', views.MusicList, name='listagem'),
    path('postMusica/', views.MusicPost, name='envio'),
    path('putMusica/<str:pk>/', views.MusicPut, name='atualizar'),
    path('deleteMusica/<str:pk>/', views.MusicDelete, name='deletar')
]