from django.shortcuts import render,get_object_or_404, redirect
from .models import Tema, Recurso
from .forms import TemaForm, RecursoForm


# Formulário para criar Tema
class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'resumo']


# Formulário para criar e editar Recurso
class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = [
            'tema',
            'nome',
            'descricao',
            'tipo',
            'url',
            'gratuito'
        ]
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

# Formulário para criar Tema
class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['titulo', 'resumo']


# Formulário para criar e editar Recurso
class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = [
            'tema',
            'nome',
            'descricao',
            'tipo',
            'url',
            'gratuito'
        ]
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
   # teste commit 
     # teste commit 
       
def votar_prestigio(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)
    recurso.prestigio += 1
    recurso.save()
    return redirect('detalhe_recurso', recurso_id=recurso.id)

def adicionar_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_temas')
    else:
        form = TemaForm()

    return render(request, 'catalogo/form.html', {'form': form})

def adicionar_recurso(request):
    if request.method == 'POST':
        form = RecursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_temas')
    else:
        form = RecursoForm()

    return render(request, 'catalogo/form.html', {'form': form})

def editar_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)

    if request.method == 'POST':
        form = RecursoForm(request.POST, instance=recurso)
        if form.is_valid():
            form.save()
            return redirect('detalhe_recurso', recurso_id=recurso.id)
    else:
        form = RecursoForm(instance=recurso)

    return render(request, 'catalogo/form.html', {'form': form})

def excluir_recurso(request, recurso_id):
    recurso = get_object_or_404(Recurso, id=recurso_id)

    if request.method == 'POST':
        recurso.delete()
        return redirect('lista_temas')

    return render(request, 'catalogo/confirmar_exclusao.html', {'recurso': recurso})
