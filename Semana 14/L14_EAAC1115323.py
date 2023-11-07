class Automovil:
    def __init__(self):
        self.modelo = 0
        self.precio = 0.0
        self.marca = ""
        self.disponible = True
        self.tipoCambio = 7.50
        self.descuentoAplicado = 0.0

    def definirModelo(self, unModelo):
        self.modelo = unModelo

    def definirPrecio(self, unPrecio):
        self.precio = unPrecio

    def definirMarca(self, unaMarca):
        self.marca = unaMarca

    def definirTipoCambio(self, unTipoCambio):
        self.tipoCambio = unTipoCambio

    def cambiarDisponibilidad(self):
        self.disponible = not self.disponible

    def mostrarDisponibilidad(self):
        return "Disponible" if self.disponible else "No se encuentra disponible actualmente"

    def mostrarInformacion(self):
        precioQuetzales = self.precio / self.tipoCambio
        return (
            f"Marca: {self.marca}. Modelo: {self.modelo}. Precio de venta: Q{precioQuetzales:.2f}. "
            f"{self.mostrarDisponibilidad()}"
        )

    def aplicarDescuento(self, miDescuento):
        self.descuentoAplicado = miDescuento
        descuento = self.precio * miDescuento
        self.precio -= descuento

def main():
    auto = Automovil()
    auto.definirModelo(2023)
    auto.definirPrecio(200000.0)
    auto.definirMarca("Toyota")
    auto.definirTipoCambio(7.50)

    print(auto.mostrarInformacion())
    auto.aplicarDescuento(0.1)
    print(auto.mostrarInformacion())

if __name__ == "__main__":
    main()