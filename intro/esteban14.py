
angulo = float(input("Introduce el ángulo en grados: "))


vueltas = angulo // 360  
angulo_restante = angulo % 360  


pi = 3.141592653589793


angulo_radianes = angulo_restante * (pi / 180)


if 0 <= angulo_restante < 90:
    cuadrante = 1
elif 90 <= angulo_restante < 180:
    cuadrante = 2
elif 180 <= angulo_restante < 270:
    cuadrante = 3
else:
    cuadrante = 4


print(f"El ángulo se encuentra en el cuadrante {cuadrante}.")
print(f"El número de vueltas completas es: {int(vueltas)}.")
print(f"El ángulo en radianes es: {angulo_radianes:.4f}.")


n = int(input("Introduce el número de términos de la serie Fibonacci: "))


a, b = 0, 1


if n <= 0:
    print("Por favor, introduce un número mayor que 0.")
else:
    print("Los primeros", n, "números de la serie Fibonacci son:")
    
    
    for _ in range(n):
        print(a)
        a, b = b, a + b  


