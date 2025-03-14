def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10  #
        n //= 10  
    return suma


n = int(input("Introduce un número entero de dos cifras: "))


resultado = suma_digitos(n)
print("La suma de los dígitos de", n, "es:", resultado)
