from django.shortcuts import render, redirect
from .models import Operacion

# Create your views here.

def formulario(request):
    if request.method == 'POST':
        numero1 = int(request.POST['numero1'])
        numero2 = int(request.POST['numero2'])
        operacion = request.POST['operacion']
        if operacion == 'suma':
            resultado = numero1 + numero2
        elif operacion == 'resta':
            resultado = numero1 - numero2
        else:
            resultado = numero1 * numero2
        Operacion.objects.create(numero1=numero1, numero2=numero2, operacion=operacion)
        return redirect('resultado', resultado=resultado)
    return render(request, 'formulario.html')

def resultado(request, resultado):
    return render(request, 'resultado.html', {'resultado': resultado})


