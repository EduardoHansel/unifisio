from django.db import models

# Create your models here.

class Paciente(models.Model):

    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'

    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    sexo = models.CharField(max_length=1, choices=Sexo.choices)
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    contato_1 = models.CharField(max_length=15, verbose_name="Contato principal")
    contato_2 = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contato secundário", default="Não informado")

    class Meta:
        # Garante que o Django use o nome de tabela exato da sua imagem
        db_table = 'pacientes'
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nome
