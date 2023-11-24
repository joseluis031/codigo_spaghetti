class OperacionesMatematicas:
    @staticmethod
    def suma(num1, num2):
        return num1 + num2

    @staticmethod
    def resta(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")

class Calculadora:
    def __init__(self):
        self.operaciones = OperacionesMatematicas()

    def obtener_numero(self, mensaje):
        while True:
            try:
                numero = float(input(mensaje))
                return numero
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def obtener_numeros(self):
        num1 = self.obtener_numero("Ingrese el primer número: ")
        num2 = self.obtener_numero("Ingrese el segundo número: ")
        return num1, num2

    def calcular(self):
        operacion = input("Ingrese la operación que desea realizar (suma, resta, multiplicacion o division): ")
        num1, num2 = self.obtener_numeros()

        if operacion == 'suma':
            resultado = self.operaciones.suma(num1, num2)
        elif operacion == 'resta':
            resultado = self.operaciones.resta(num1, num2)
        elif operacion == 'multiplicacion':
            resultado = self.operaciones.multiplicacion(num1, num2)
        elif operacion == 'division':
            resultado = self.operaciones.division(num1, num2)
        else:
            print("Operación no soportada.")
            resultado = None

        return resultado

# Crear una instancia de la clase Calculadora y llamar al método calcular
calculadora = Calculadora()
resultado_calculado = calculadora.calcular()
print("El resultado es:", resultado_calculado)
