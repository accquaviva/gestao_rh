from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from apps.funcionarios.models import Funcionario
from django.views.generic.list import ListView

#funcionario_list
class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

#funcionario_form
class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


