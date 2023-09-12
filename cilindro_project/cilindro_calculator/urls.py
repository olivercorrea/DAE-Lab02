from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_volumen, name='calcular_volumen'),
]

