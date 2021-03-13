from django.contrib import admin
from .models import Livro

# Register your models here.
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'finalizado', 'resenha')
admin.site.register(Livro,LivroAdmin)

