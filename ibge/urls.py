from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_ibge, name='home'),
    path('busca/', views.busca, name='busca'),
    path('ranking/', views.ranking, name='ranking'),
    path('ranking_m/', views.ranking_m, name='ranking_m'),
    path('ranking_f/', views.ranking_f, name='ranking_f'),
    path('ranking_decada/', views.ranking_decada, name='ranking_decada'),
    path('curiosidades/', views.curiosidades, name='curiosidades'),
]