from django.urls import path, include
from .views import CreateDepartamento,ListDepartamento,Edit_departamento,Delete_departamento

urlpatterns = [
    path('',ListDepartamento.as_view(),name='Lista_Departamento'),
    path('novo/',CreateDepartamento.as_view(), name='Create_Departamento'),
    path('edit/<int:pk>/',Edit_departamento.as_view(),name='edit_departamento'),
    path('delete/<int:pk>/',Delete_departamento.as_view(),name='delete_departamento'),
]
