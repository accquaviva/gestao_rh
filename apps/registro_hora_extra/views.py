from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView

from apps.registro_hora_extra.forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra


class ListHoraExtra(ListView):
    model = RegistroHoraExtra
    fields = ['motivo','funcionario','horas']

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class CreateHoraExtra(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(CreateHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class EditHoraExtra(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(EditHoraExtra, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class DeleteHoraExtra(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('lista_hora_extra')

