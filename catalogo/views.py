from django.shortcuts import render,get_object_or_404
from .models import Tema, Recurso
# Create your views here.
 
# c) Painel de Assuntos
def lista_temas(request):
    temas = Tema.objects.all()
    return render(request, 'catalogo/temas.html', {'temas': temas})


# d) Vitrine do Eixo
def recursos_por_tema(request, tema_id):
    tema = get_object_or_404(Tema, id=tema_id)
    recursos = tema.recursos.order_by('-prestigio')
    return render(request, 'catalogo/recursos_tema.html', {
        'tema': tema,
        'recursos': recursos
    })


# e) Raio-X do Recurso
def detalhe_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    return render(request, 'catalogo/detalhe_recurso.html', {
        'recurso': recurso
    })