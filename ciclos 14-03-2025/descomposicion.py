def descomponer_factores_primos(n):
    for divisor in range(2, n + 1):
        while n % divisor == 0:
            print(divisor, end=" ")
            n //= divisor

n = int(input("Ingrese un número: "))
descomponer_factores_primos(n)
