class Tablero:
    def __init__(self):
        self.tableros_anteriores = []  
        self.tablero = [["!_" for _ in range(10)] for _ in range(10)]
        self.filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.columnas = [str(i) for i in range(1, 11)]

    def mostrar_tablero(self, disparos_realizados):
        print("   " + "  ".join(self.columnas))
        for i, fila in enumerate(self.tablero):
            fila_mostrar = []
            for j, casilla in enumerate(fila):
                if (i, j) in disparos_realizados:
                    fila_mostrar.append(" ☻" if casilla == " ♠" else " ☼" if casilla == " ♥" else " •")
                else:
                    fila_mostrar.append(casilla)
            print(self.filas[i] + " " + " ".join(fila_mostrar))

    def mostrar_tablero_oculto(self, barcos, disparos_realizados):
        tablero_oculto = [["!_" for _ in range(10)] for _ in range(10)]

        for barco in barcos:
            if barco.orientación == "v":
                for j in range(barco.tamaño):
                    if barco.tocado[j]:
                        tablero_oculto[barco.fila + j][barco.columna] = " ♥" if not barco.barco_hundido() else " X"
            else:
                for j in range(barco.tamaño):
                    if barco.tocado[j]:
                        tablero_oculto[barco.fila][barco.columna + j] = " ♥" if not barco.barco_hundido() else " X"

        for disparo in disparos_realizados:
            fila, columna = disparo
            if tablero_oculto[fila][columna] == "!_":
                tablero_oculto[fila][columna] = " ☻"

        print("   " + "  ".join(self.columnas))
        for i, fila in enumerate(tablero_oculto):
            print(self.filas[i] + " " + " ".join(fila))
        self.tableros_anteriores.append([fila[:] for fila in self.tablero])

    def deshacer_ultimo_disparo(self):
        if self.tableros_anteriores:
            self.tablero = [fila[:] for fila in self.tableros_anteriores.pop()]

    def reiniciar_tableros(self):
        self.tableros_anteriores = []
        self.tablero = [["!_" for _ in range(10)] for _ in range(10)]


class Barco:
    def __init__(self, tamaño, orientación, fila, columna):
        self.tamaño = tamaño
        self.orientación = orientación
        self.fila = fila
        self.columna = columna
        self.tocado = [False] * tamaño

    def barco_hundido(self):
        return all(self.tocado)


class Juego:
    def __init__(self):
        self.jugador1 = Tablero()
        self.jugador2 = Tablero()
        self.barcos1 = []
        self.barcos2 = []
        self.disparos_realizados1 = []  
        self.disparos_realizados2 = []  
        self.turno = 0
        self.ganador = None

    def ubicacion_valida(self, tablero_jugador, barco):
        if barco.orientación == "v":
            if barco.fila + barco.tamaño > 10:
                return False
            for i in range(barco.tamaño):
                if tablero_jugador.tablero[barco.fila + i][barco.columna] != "!_":
                    return False
        else:
            if barco.columna + barco.tamaño > 10:
                return False
            for i in range(barco.tamaño):
                if tablero_jugador.tablero[barco.fila][barco.columna + i] != "!_":
                    return False
        return True

    def convertir_coordenadas(self, fila, columna):
        filas = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
        fila = fila.upper()
        fila_num = filas.get(fila, None)
        if fila_num is None or columna < 1 or columna > 10:
            return None
        return fila_num, columna - 1

    def ubicar_barcos_jugador(self, jugador, barcos):
        tablero = self.jugador1 if jugador == 1 else self.jugador2
        barcos_lista = self.barcos1 if jugador == 1 else self.barcos2
        print(f"Jugador {jugador}, coloca tus barcos:")
        for barco_tamaño in barcos:
                while True:
                    tablero.mostrar_tablero([])
                    fila = input(f"Ingrese la fila para el barco de tamaño {barco_tamaño}, (A-J): ")
                    columna = int(input(f"Ingrese la columna para el barco de tamaño {barco_tamaño}, (1-10): "))
                    orientacion = input("Ingrese la orientación (vertical(v) u horizontal(h)): ").lower()

                    coordenadas = self.convertir_coordenadas(fila, columna)
                    if coordenadas is not None:
                        fila, columna = coordenadas
                        nuevo_barco = Barco(barco_tamaño, orientacion, fila, columna)
                        if self.ubicacion_valida(tablero, nuevo_barco):
                            tablero.tablero[fila][columna] = " ♠"
                            if orientacion == "v":
                                for j in range(1, barco_tamaño):
                                    tablero.tablero[fila + j][columna] = " ♠"
                            else:
                                for j in range(1, barco_tamaño):
                                    tablero.tablero[fila][columna + j] = " ♠"
                            barcos_lista.append(nuevo_barco)
                            break
                        else:
                            print("Ubicación inválida, intente de nuevo.")
                    else:
                        print("Coordenadas inválidas, intente de nuevo.")

    def realizar_disparo(self, jugador, fila, columna):
        if jugador == 1:
            tablero = self.jugador2
            barcos_enemigos = self.barcos2
            disparos_realizados = self.disparos_realizados1
        else:
            tablero = self.jugador1
            barcos_enemigos = self.barcos1
            disparos_realizados = self.disparos_realizados2

        if (fila, columna) in disparos_realizados:
            return "Repetido"

        disparos_realizados.append((fila, columna))

        if tablero.tablero[fila][columna] == " ♠":
            for barco in barcos_enemigos:
                if barco.orientación == "v":
                    if barco.fila <= fila < barco.fila + barco.tamaño and barco.columna == columna:
                        barco.tocado[fila - barco.fila] = True
                        if barco.barco_hundido():
                            return "Hundido"
                        return "Tocado"
                else:
                    if barco.columna <= columna < barco.columna + barco.tamaño and barco.fila == fila:
                        barco.tocado[columna - barco.columna] = True
                        if barco.barco_hundido():
                            return "Hundido"
                        return "Tocado"
        else:
            return "Agua"

    def jugar(self):
        self.ubicar_barcos_jugador(1, [5, 5, 3, 3, 3])
        self.ubicar_barcos_jugador(2, [5, 5, 3, 3, 3])

        while not self.ganador:
            print(f"Turno del Jugador {self.turno % 2 + 1}")
            fila = input("Ingrese la fila para disparar (A-J): ")
            columna = int(input("Ingrese la columna para disparar (1-10): "))

            coords = self.convertir_coordenadas(fila, columna)
            if coords is not None:
                resultado = self.realizar_disparo(self.turno % 2 + 1, *coords)
                self.jugador2.mostrar_tablero_oculto(self.barcos2, self.disparos_realizados2)
                print("\nDisparo realizado en", fila, columna)
                print("\n-----------------\n")
                if resultado == "Repetido":
                    print("¡Ya has disparado aquí!")
                elif resultado == "Hundido":
                    print("¡Barco hundido!")
                elif resultado == "Tocado":
                    print("¡Barco tocado!")
                elif resultado == "Agua":
                    print("¡Agua, intenta de nuevo!")

                if resultado != "Repetido":
                    self.turno += 1

            if all(barco.barco_hundido() for barco in self.barcos1):
                self.ganador = "Jugador 1"
            elif all(barco.barco_hundido() for barco in self.barcos2):
                self.ganador = "Jugador 2"

        print(f"¡El ganador es {self.ganador}!")

juego_batalla_naval = Juego()
juego_batalla_naval.jugar()
