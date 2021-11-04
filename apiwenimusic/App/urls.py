from django.urls import path
from App import views
from . import views

urlpatterns = [
    path('Musica/', views.MusicPost.as_view()),
    path('Musica/<str:pk>/', views.MusicViewSet.as_view()),

    path('Artista/', views.ArtistaPost.as_view()),
    path('Artista/<str:pk>/', views.ArtistaViewSet.as_view()),

    path('Playlist/', views.PlaylistPost.as_view()),
    path('Playlist/<str:pk>/', views.PlaylistViewSet.as_view())
]