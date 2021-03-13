from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import NovoLivroForm
#API
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import LivroSerializer

# Create your views here.
def index(request):
    livros = Livro.objects.all()
    return render(request, 'livros/lista.html', {'livros': livros})

def detalhes(request,id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'livros/detalhes.html', {'livro': livro})

def criar(request):
    if request.method == 'POST':
        form = NovoLivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = NovoLivroForm()
    return render(request, 'livros/novo.html', {'form': form})

def editar(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == 'GET':
        form = NovoLivroForm(instance=livro)
        return render(request, 'livros/novo.html', {'form': form})
    else:
        form = NovoLivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('index')

def excluir(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('index')
    return render(request, 'livros/excluir.html', {'livro': livro})

# Views da api.
class listarLivros(ListAPIView):
    """Lista todos os livros cadastrados"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class detalharLivro(RetrieveAPIView):
    """Exibe os detalhes de um livro"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class criarLivro(CreateAPIView):
    """Cria um novo livro"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class atualizarLivro(UpdateAPIView):
    """Atualiza o livro selecionado"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class removerLivro(DestroyAPIView):
    """Remove o livro selecionado"""
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer