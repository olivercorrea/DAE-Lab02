from django.shortcuts import render
from math import pi
# Create your views here.

def calcular_volumen(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = pi * radio ** 2 * altura
        return render(request, 'resultado.html', {'volumen': volumen})
    return render(request, 'formulario.html')


