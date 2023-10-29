class Calculadora:
    def __init__(self):
        self.num1 = ""
        self.num2 = ""

    def insertar_num1(self, num1):
        self.num1 = num1

    def insertar_num2(self, num2):
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"
        
calc = Calculadora()
num1 = float(input("Por favor ingrese el primer número: "))
num2 = float(input("Por favor ingrese el segundo número: "))
calc.insertar_num1(num1)
calc.insertar_num2(num2)

while True:
    print()
    print("Menú:")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    opcion = int(input("Seleccione una opción (escriba el número de la opción): "))
    if opcion == 1:
        print("Resultado: ", calc.suma())
    elif opcion == 2:
        print("Resultado: ", calc.resta())
    elif opcion == 3:
        print("Resultado: ", calc.multiplicacion())
    elif opcion == 4:
        print("Resultado: ", calc.division())
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")