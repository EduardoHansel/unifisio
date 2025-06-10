from django.db import models

# Create your models here.

class Paciente(models.Model):

    class Sexo(models.TextChoices):
        MASCULINO = "Masculino"
        FEMININO = "Feminino"

    funcionario_criacao_id = models.IntegerField(blank=True, null=True)
    primeiro_nome = models.CharField(max_length=100, verbose_name="Primeiro nome")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome")
    cpf = models.CharField(max_length=11, verbose_name="CPF", unique=True)
    sexo = models.CharField(max_length=9, choices=Sexo.choices)
    data_nascimento = models.DateField(verbose_name="Data de nascimento")
    contato_1 = models.CharField(max_length=15, verbose_name="Contato principal")
    contato_2 = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contato secundário")

    class Meta:
        db_table = "pacientes"
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.primeiro_nome
