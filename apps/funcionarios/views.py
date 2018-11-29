from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

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


class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split()[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionarioNovo,self).form_valid(form)

