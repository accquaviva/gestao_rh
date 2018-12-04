from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView

from apps.registro_hora_extra.models import RegistroHoraExtra


class ListHoraExtra(ListView):
    model = RegistroHoraExtra
    fields = ['motivo','funcionario','horas']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class CreateHoraExtra(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class EditHoraExtra(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class DeleteHoraExtra(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('lista_hora_extra')

