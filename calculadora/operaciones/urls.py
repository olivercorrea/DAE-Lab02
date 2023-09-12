from django.urls import path
from . import views

urlpatterns = [
    path('formulario/', views.formulario, name='formulario'),
    path('resultado/<int:resultado>/', views.resultado, name='resultado'),
]
