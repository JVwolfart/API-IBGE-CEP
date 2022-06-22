from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_cep, name='home_cep'),
    path('consulta_cep/', views.consulta_cep, name='consulta_cep'),
    path('consulta_rua/', views.consulta_rua, name='consulta_rua'),
    path('detalhes/<str:cep>', views.detalhes, name='detalhes'),
]