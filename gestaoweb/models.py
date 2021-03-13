from django.db import models

# Create your models here.
class Livro(models.Model):
    nome        = models.CharField('Nome',max_length=100)
    finalizado  = models.BooleanField('Já finalizado')
    resenha     = models.TextField('Resenha', null=True, blank=True)

    def __str__(self):
        return self.nome
