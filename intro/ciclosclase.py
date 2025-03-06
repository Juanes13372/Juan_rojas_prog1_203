

n = int(input("Introduce el número de términos de la serie Fibonacci: "))

a, b = 0, 1


if n <= 0:
    print("Por favor, introduce un número mayor que 0.")
else:
    print("Los primeros", n, "números de la serie Fibonacci son:")
    
    
    for _ in range(n):
        print(a)
        a, b = b, a + b  
