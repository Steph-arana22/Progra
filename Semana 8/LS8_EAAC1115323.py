print("Menú:")
print("1. Factorial")
print("2. Secuencia de Fibonacci")
print ("3. Salir")
x=input("Por favor ingrese el número de opción que quiere ejecutar: ")
x=int(x)
if x==1:
   y=input("ingrese un número: ")
   y=int(y)
def calcular_factorial(y):
   n=1
   for i in range (1,y+1):
      n*=i
      return n

resultado1= calcular_factorial(y)
print(str(y) +"="+ str(y)+"*" +str(y - 1)+"* ... * 2 * 1 =" + resultado1 )

    #print(f"{str(y)} = {str(y)} * {str(y - 1)} * ... * 2 * 1 = {Resultado}")*/

