cadena = input("Por favor, introduce una cadena de caracteres: ")
unos = cadena.count('1')
ceros = cadena.count('0')
otros = len(cadena) - unos - ceros 
print("La cadena contiene", unos, "1's")
print("La cadena contiene", ceros, "0's")
print("La cadena contiene", otros, "otros caracteres")

#Count es un método que devuelve el número de veces que el valor especificado aparece en cadena de texto.