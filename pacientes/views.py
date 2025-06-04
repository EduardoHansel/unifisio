from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Paciente

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World")

@csrf_exempt
def criar_paciente(request):
    if request.method == 'POST':
        nome_do_paciente = request.POST.get("nome")
        cpf_do_paciente = request.POST.get("cpf")
        sexo_do_paciente = request.POST.get("sexo")
        data_de_mascimento_paciente = request.POST.get("data_nascimento")
        contato_1_paciente = request.POST.get("contato_1")
        contato_2_paciente = request.POST.get("contato_2")

        if nome_do_paciente and cpf_do_paciente and sexo_do_paciente and data_de_mascimento_paciente and contato_1_paciente and contato_2_paciente:
            novo_paciente = Paciente(nome=nome_do_paciente, cpf=cpf_do_paciente, sexo=sexo_do_paciente, data_nascimento=data_de_mascimento_paciente, contato_1=contato_1_paciente, contato_2=contato_2_paciente)
            print(f"Novo paciente criado: {novo_paciente.nome}")
            print(f"Total de pacientes na lista: {len(Paciente.lista_pacientes)}")

            dados_resposta = {
                'id': Paciente.current_id,
                'nome': novo_paciente.nome,
                'cpf': novo_paciente.cpf,
                'message': 'Paciente criado com sucesso!'
            }

            return JsonResponse(dados_resposta, status=201)
        else:
            return JsonResponse({'error': 'Nome e CPF são campos obrigatórios.'}, status=400)
    return JsonResponse({'error': 'Método GET não é permitido para esta URL'}, status=405)
