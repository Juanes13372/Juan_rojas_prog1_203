def imprimir_triangulo(n):
    
    for i in range(1, n + 1):

        for j in range(i):
            print(i, end="") 
        print() 


n = int(input("Ingrese el número de filas: "))


imprimir_triangulo(n)
