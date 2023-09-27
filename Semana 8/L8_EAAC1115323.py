w=""
while w !=3:
    print("Menú:")
    print("1. Factorial")
    print("2. Secuencia de Fibonacci")
    print ("3. Salir")
    x=input("Por favor ingrese el número de opción que quiere ejecutar: ")
    x=int(x)
    if x==1:
        y=int(input("Ingrese un número: "))
        resultado1=1
        for i in range (1,y+1):
            resultado1 *= i
            print(str(y) +"="+ str(y)+"* ... * 2 * 1 =" + str(resultado1))
    elif x == 2:
            z = int(input("Ingrese un número: "))
            a, b = 0, 1
            count = 0
            print(a, end=", ")
            print(b, end=", ")
            while count < z:
                n= a + b
                print(n, end=", ")
                a = b
                b = n
                count += 1
    elif x == 3:
            print("Saliendo del programa...") 
    else:
            print("opción incorrecta. Por favor ingresar un número de las opciones del menú.")
