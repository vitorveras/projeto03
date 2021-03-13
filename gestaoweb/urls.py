from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', views.index, name='index'),
    path('livro/<int:id>', views.detalhes, name='detalhes'),
    path('livro/novo', views.criar, name='novo'),
    path('livro/editar/<int:id>', views.editar, name='editar'),
    path('livro/excluir/<int:id>', views.excluir, name='excluir'),
    #API
    path('livro/api/doc/',include_docs_urls(title='Livro Api')),
    path("livro/api/",views.listarLivros.as_view(),name="listar_livros_api"),
    path("livro/api/<int:pk>/",views.detalharLivro.as_view(),name="detalhar_livro_api"),
    path("livro/api/novo/", views.criarLivro.as_view(),name="novo_livro_api"),
    path("livro/api/editar/<int:pk>/",views.atualizarLivro.as_view(),name="atualizar_livro_api"),
    path("livro/api/excluir/<int:pk>/",views.removerLivro.as_view(),name="excluir_livro_api"),
]