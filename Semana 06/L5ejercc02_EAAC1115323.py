#Ejercicio 02
x = input("Por favor ingrese un número de día: ")
x = int(x)
d=""
if x<0 or x>7:
    d="Error, el número a ingresar debe estar contenido entre 1 y 7"
elif x==1:
    d="lunes"
elif x==2:
    d="martes"
elif x==3:
    d="miercoles"
elif x==4:
    d="jueves"
elif x==5:
    d="viernes"
elif x==6:
    d="sabado"
else:
    d="domingo"

print("Día: " +d)