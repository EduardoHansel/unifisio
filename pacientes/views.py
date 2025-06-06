import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import PacienteForm
from .models import Paciente

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World")

@csrf_exempt
@require_http_methods(["POST"])
def criar_paciente(request):
    try:
        data = json.loads(request.body)
        form = PacienteForm(data)

        if form.is_valid():
            novo_paciente = form.save()

            print(f"Novo paciente salvo no banco de dados: {novo_paciente.nome}, ID: {novo_paciente.id}")

            dados_resposta = {
                'id': novo_paciente.id,
                'nome': novo_paciente.nome,
                'cpf': novo_paciente.cpf,
                'message': 'Paciente criado com sucesso'
            }
            return JsonResponse(dados_resposta, status=201)
        else:
            # Se o formulário for inválido, retorna os erros de validação
            return JsonResponse({'errors': form.errors}, status=400)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Corpo da requisição JSON inválido.'}, status=400)
    except Exception as e:
        # Captura outros erros inesperados
        return JsonResponse({'error': f'Ocorreu um erro interno: {str(e)}'}, status=500)

def listar_pacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()

        data = list(pacientes.values('id', 'nome', 'cpf', 'sexo', 'data_nascimento', 'contato_1', 'contato_2'))

        return JsonResponse(data, safe=False)
