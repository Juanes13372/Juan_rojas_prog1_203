import random


def generar_numero():
    return random.randint(1, 100)
print(generar_numero)


def jugar_adivinanza():
    num= generar_numero()
    num2 = 0
    cont = 0

    
    while num != num2:
        num2 = int(input("Adivina el valor (entre 1 y 100): "))
        cont += 1
        
        
        if num2 < num:
            print("El número es mayor. Intenta de nuevo.")
        elif num2 > num:
            print("El número es menor. Intenta de nuevo.")
    
    
    print(f"¡Felicidades! Adivinaste el número en {cont} intentos.")

jugar_adivinanza()
