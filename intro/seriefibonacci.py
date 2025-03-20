def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a)
        a, b = b, a + b

n = int(input("Digite hasta qué número desea su serie Fibonacci: "))
fibonacci(n)
