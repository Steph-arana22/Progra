#Ejercicio 01
x = input("Por favor ingrese un número entero: ")
x = int(x)
c = ""
if x < 0:
    c = "Es un número negativo"
elif x > 0:
    c = "Es un número positivo"
else:
    c = "El número es igual a 0"

print("Resultado: " +c)