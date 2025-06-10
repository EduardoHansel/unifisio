from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['primeiro_nome', 'sobrenome', 'cpf', 'sexo', 'data_nascimento', 'contato_1', 'contato_2']
