# Definimos una función para solicitar la información de cada línea de producción
def solicitar_info_linea(num_linea):
    print()
    precio_venta = int(input(f'Ingrese el precio de venta por metro cuadrado para la línea {num_linea}: '))
    metros_vendidos = int(input(f'Ingrese la cantidad de metros cuadrados vendidos para la línea {num_linea}:'))
    print()
    print(f'---Resultados línea {num_linea}---')
    print(f'Precio de venta por metro cuadrado: '+str(precio_venta))
    print(f'cantidad de metros cuadrados vendidos: '+str(metros_vendidos))

    empleados = []
    for i in range(20):  # Máximo de 20 empleados
        horas = int(input(f'Ingrese las horas trabajadas por el empleado {i+1} en la línea {num_linea}, o -1 si no hay más empleados: '))
        horass=horas
        if horas == -1:
            break
        costo_hora = int(input(f'Ingrese el costo por hora del empleado {i+1} en la línea {num_linea}: '))

        print(f'horas trabajadas por el empleado {i+1}: '+str(horass))
        print(f'costo por hora del empleado {i+1}: '+str(costo_hora))
        empleados.append((horas, costo_hora))
    return precio_venta, metros_vendidos, empleados

# Solicitamos la información de las dos líneas de producción
info_linea1 = solicitar_info_linea(1)
info_linea2 = solicitar_info_linea(2)

# Definimos una función para realizar los cálculos
def calcular_ganancias_costos(info_linea):
    precio_venta, metros_vendidos, empleados = info_linea
    ganancia_total = precio_venta * metros_vendidos
    costo_total = sum(horas * costo_hora for horas, costo_hora in empleados)
    ganancia_neta = ganancia_total - costo_total
    indice_eficiencia = ganancia_neta / len(empleados)
    print(f'---Resultados línea---')
    print(f'Ganancia total: '+str(ganancia_total))
    print(f'Costo total: '+str(costo_total))
    print(f'Ganancia neta: '+str(ganancia_neta))
    print(f'Indice de eficiencia: '+str(indice_eficiencia))
    print()
    return ganancia_total, costo_total, ganancia_neta, indice_eficiencia

# Calculamos las ganancias, costos e índice de eficiencia para cada línea de producción
ganancias_costos_linea1 = calcular_ganancias_costos(info_linea1)
ganancias_costos_linea2 = calcular_ganancias_costos(info_linea2)

# Determinamos cuál línea de producción tiene el mayor índice de eficiencia
if ganancias_costos_linea1[3] > ganancias_costos_linea2[3]:
    print('---Índice de eficiencia---')
    print('La línea 1 tiene el mayor índice de eficiencia.')
elif ganancias_costos_linea1[3] < ganancias_costos_linea2[3]:
    print('---Índice de eficiencia---')
    print('La línea 2 tiene el mayor índice de eficiencia.')
else:
    print('---Índice de eficiencia---')
    print('Las dos líneas de producción tienen el mismo índice de eficiencia.')