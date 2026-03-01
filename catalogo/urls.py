from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_temas, name='lista_temas'),
    path('tema/<int:tema_id>/', views.recursos_por_tema, name='recursos_por_tema'),
    path('recurso/<int:recurso_id>/', views.detalhe_recurso, name='detalhe_recurso'),

    # --- LISTA 15 (ACRESCENTAR) ---

    path('tema/novo/', views.adicionar_tema, name='adicionar_tema'),
    path('recurso/novo/', views.adicionar_recurso, name='adicionar_recurso'),
    path('recurso/<int:recurso_id>/votar/', views.votar_prestigio, name='votar_prestigio'),
    path('recurso/<int:recurso_id>/editar/', views.editar_recurso, name='editar_recurso'),
    path('recurso/<int:recurso_id>/excluir/', views.excluir_recurso, name='excluir_recurso'),
    
    ]