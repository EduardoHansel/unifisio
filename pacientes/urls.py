from django.urls import path
from . import views

urlpatterns = [
    path("novo_paciente/", views.criar_paciente),
    path("<int:pk>/alterar/", views.alterar_paciente),
    path("<int:pk>/deletar/", views.deletar_paciente),
    path("listar_pacientes/", views.listar_pacientes),
]
