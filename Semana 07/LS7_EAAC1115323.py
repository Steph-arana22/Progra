print("Ejercicio 1: operaciones aritméticas")
x=input("Por favor ingrese un número: ")
y=input("Por favor ingrese otro número: ")
z=""
while z!="fin":
    z=input("Ingrese la operación que desea (suma, resta, multiplicación, división, módulo, exponencial o cociente) si desea que finalice ingresa (fin): ")
    x=int(x)
    y=int(y)
    suma=x+y
    resta=x-y
    multiplicación=x*y
    división=x/y
    módulo=x%y
    exponencial=x**y
    cociente=x//y

    if z=="suma":
        print(str(x)+"+"+str(y)+"="+str(suma))
    elif z=="resta":
        print(str(x)+"-"+str(y)+"="+str(resta))
    elif z=="multiplicación":
        print(str(x)+"*"+str(y)+"="+str(multiplicación))
    elif z=="división":
        print(str(x)+"/"+str(y)+"="+str(división))
    elif z=="módulo":
        print(str(x)+"%"+str(y)+"="+str(módulo))
    elif z=="exponencial":
        print(str(x)+"**"+str(y)+"="+str(exponencial))
    elif z=="cociente":
        print(str(x)+"//"+str(y)+"="+str(cociente))
    elif z=="fin":
        print("A finalizado el programa")

