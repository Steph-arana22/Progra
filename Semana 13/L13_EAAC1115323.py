class Circulo:
    def __init__(self, radio):
        self.radio = radio

    # Obtener perímetro
    def calcular_perimetro(self):
        return 2 * 3.1416 * self.radio

    # Obtener área
    def calcular_area(self):
        return 3.1416 * self.radio ** 2

    # Obtener volumen
    def calcular_volumen(self):
        return (4 * 3.1416 * self.radio ** 3) / 3

radio = float(input("Ingresa un valor de radio: "))
Circulo1 = Circulo(radio)
perimetro = Circulo1.calcular_perimetro()
area = Circulo1.calcular_area()
volumen = Circulo1.calcular_volumen()

print("Radio del círculo:", radio)
print("Perímetro:", perimetro)
print("Área:", area)
print("Volumen:", volumen)