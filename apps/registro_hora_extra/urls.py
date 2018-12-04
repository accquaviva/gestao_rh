from django.urls import path, include
from .views import ListHoraExtra, CreateHoraExtra, EditHoraExtra,DeleteHoraExtra

urlpatterns = [
    path('', ListHoraExtra.as_view(), name='lista_hora_extra'),
    path('novo', CreateHoraExtra.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', EditHoraExtra.as_view(), name='edit_hora_extra'),
    path('deletar/<int:pk>',DeleteHoraExtra.as_view(),name='delete_hora_extra'),
]
