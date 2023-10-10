n= int(input("Por favor ingrese un número decimal: "))
def decimal_a_hexadecimal(n):
    hexadecimal = ['0'] * 100
    i=0
    while(n != 0): 
        x = 0
        x = n % 16
        if(x < 10): 
            hexadecimal[i] = chr(x + 48) 
            i = i + 1
        else: 
            hexadecimal[i] = chr(x + 55) 
            i = i + 1
        n = int(n / 16) 
    j = i - 1
    while(j >= 0): 
        print((hexadecimal[j]), end="") 
        j = j - 1

decimal_a_hexadecimal(n)