from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'calculator/ruben.html')

@csrf_exempt
def calcular(request):
    if request.method == 'POST':
        operacion = request.POST['operacion']
        num1 = obtener_numero(request.POST['num1'])
        num2 = obtener_numero(request.POST['num2'])
        resultado = None

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "No se puede dividir entre cero."
        else:
            resultado = "Operación no soportada."

        return render(request, 'calculator/calcular.html', {'resultado': resultado})

    return HttpResponse(status=400)

def obtener_numero(valor):
    try:
        return float(valor)
    except ValueError:
        return "Por favor, ingrese un número válido."

