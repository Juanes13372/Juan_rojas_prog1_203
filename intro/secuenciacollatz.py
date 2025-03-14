n = int(input("Ingrese un valor: "))


for i in range(2, n + 1):
    if i % 2 == 0:  
        par = i // 2  
        print(f"Cuando el número es par ({i}), la mitad es {par}")
    else:  
        resultado = i * 3 + 1  
        print(f"Cuando el número es impar ({i}), el resultado de 3 * {i} + 1 es {resultado}")
