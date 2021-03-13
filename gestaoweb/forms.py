from django import forms
from .models import Livro
#DataFlair
class NovoLivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'