import json
from .forms import PacienteForm
from .models import Paciente
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def criar_paciente(request):

    try:
        data = json.loads(request.body)
        form = PacienteForm(data)

        if form.is_valid():
            novo_paciente = form.save()
            print(f"Novo paciente salvo no banco de dados: {novo_paciente.primeiro_nome}, ID: {novo_paciente.id}")

            dados_resposta = {
                'id': novo_paciente.id,
                'primeiro_nome': novo_paciente.primeiro_nome,
                'cpf': novo_paciente.cpf,
                'message': 'Paciente criado com sucesso'
            }
            return JsonResponse(dados_resposta, status=201)

        else:
            return JsonResponse({'errors': form.errors}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Corpo da requisição JSON inválido.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Ocorreu um erro interno: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["PUT"])
def alterar_paciente(request, pk):

    try:
        paciente = Paciente.objects.get(pk=pk)
        data = json.loads(request.body)
        form = PacienteForm(data, instance=paciente)

        if form.is_valid():
            paciente_atualizado = form.save()

            dados_resposta = {
                'id': paciente_atualizado.id,
                'primeiro_nome': paciente_atualizado.primeiro_nome,
                'cpf': paciente_atualizado.cpf,
                'message': 'Paciente atualizado com sucesso'
            }
            return JsonResponse(dados_resposta, status=200)

        else:
            return JsonResponse({'errors': form.errors}, status=400)

    except Paciente.DoesNotExist:
        return JsonResponse({'error': 'Paciente não encontrado.'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Corpo da requisição JSON inválido.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Ocorreu um erro interno: {str(e)}'}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def deletar_paciente(request, pk):

    try:
        paciente = Paciente.objects.get(pk=pk)
        paciente.delete()
        return HttpResponse(status=204)

    except Paciente.DoesNotExist:
        return JsonResponse({'error': 'Paciente não encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Ocorreu um erro interno: {str(e)}'}, status=500)


def listar_pacientes(request):

    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        data = list(pacientes.values('id', 'primeiro_nome', 'sobrenome', 'cpf', 'sexo', 'data_nascimento', 'contato_1', 'contato_2'))
        return JsonResponse(data, safe=False)
