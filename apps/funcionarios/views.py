from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import UpdateView

from apps.funcionarios.models import Funcionario
from django.views.generic.list import ListView

class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

