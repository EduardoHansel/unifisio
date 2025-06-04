from django.db import models

# Create your models here.

class Paciente:
    lista_pacientes = []
    current_id = 1
    """Essa é a classe que gerará as instâncias de cada paciente no sistema"""

    def __init__(self, nome, cpf, sexo, data_nascimento, contato_1, contato_2):
        self.id_db = Paciente.current_id
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.contato_1 = contato_1
        self.contato_2 = contato_2
        Paciente.lista_pacientes.append(self)
        Paciente.current_id += 1
