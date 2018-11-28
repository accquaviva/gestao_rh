from apps.funcionarios.models import Funcionario
from django.views.generic.list import ListView

class FuncionarioList(ListView):
    model = Funcionario


