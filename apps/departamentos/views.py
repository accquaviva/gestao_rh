from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,DeleteView
from .models import Departamento
from django.views.generic.list import ListView




class ListDepartamento(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class CreateDepartamento(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()

        return super(CreateDepartamento,self).form_valid(form)

class Edit_departamento(UpdateView):
    model = Departamento
    fields = ['nome']

class Delete_departamento(DeleteView):
    model = Departamento
    success_url = reverse_lazy('Lista_Departamento')


