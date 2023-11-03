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

def main():
    circulos = []
    cantidad_circulos = int(input("Ingresa la cantidad de círculos que deseas crear: "))

    for i in range(cantidad_circulos):
        radio = float(input(f"Ingresa el radio del círculo {i + 1}: "))
        circulo = Circulo(radio)
        circulos.append(circulo)

    for circulo in circulos:
        perimetro = circulo.calcular_perimetro()
        area = circulo.calcular_area()
        volumen = circulo.calcular_volumen()
        
        print()
        print("Radio del círculo:", circulo.radio)
        print("Perímetro:", perimetro)
        print("Área:", area)
        print("Volumen:", volumen)

if __name__ == "__main__":
    main()