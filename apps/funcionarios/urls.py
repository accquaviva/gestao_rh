from django.urls import path, include
from .views import FuncionarioList,FuncionarioEdit,FuncionarioDelete,FuncionarioNovo

urlpatterns = [
    path('', FuncionarioList.as_view(), name='list_funcionarios'),
    path('novo', FuncionarioNovo.as_view(), name='novo_funcionarios'),
    path('editar/<int:pk>/',FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/',FuncionarioDelete.as_view(), name='delete_funcionario'),
]
