from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_temas, name='lista_temas'),
    path('tema/<int:tema_id>/', views.recursos_por_tema, name='recursos_por_tema'),
    path('recurso/<int:recurso_id>/', views.detalhe_recurso, name='detalhe_recurso'),
]