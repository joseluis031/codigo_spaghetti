def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un número válido.")

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("No se puede dividir entre cero.")

def obtener_numeros():
    num1 = obtener_numero("Ingrese el primer número: ")
    num2 = obtener_numero("Ingrese el segundo número: ")
    return num1, num2

def calcular():
    operacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion o division): ")
    num1, num2 = obtener_numeros()
    
    if operacion == 'suma':
        resultado = suma(num1, num2)
    elif operacion == 'resta':
        resultado = resta(num1, num2)
    elif operacion == 'multiplicacion':
        resultado = multiplicacion(num1, num2)
    elif operacion == 'division':
        resultado = division(num1, num2)
    else:
        print("Operación no soportada.")
        resultado = None

    return resultado

# Llamamos a la función calcular y mostramos el resultado
resultado_calculado = calcular()
print("El resultado es:", resultado_calculado)
