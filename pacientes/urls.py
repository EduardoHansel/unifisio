from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("novo_paciente/", views.criar_paciente)

]