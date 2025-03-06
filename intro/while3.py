
n = int(input("Introduce un número entero positivo: "))


original = n
factor = 2


print(f"Los factores primos de {original} son:", end=" ")
while n > 1:
    if n % factor == 0:  
        print(factor, end=" ")  
        n //= factor  
    else:
        factor += 1  

print()  
