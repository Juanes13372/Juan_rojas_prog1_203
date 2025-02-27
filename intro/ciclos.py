
inicio = int(input("Ingrese el valor de inicio (1-100): "))
terminacion = int(input("Ingrese el valor de terminación (1-100): "))
incremento = int(input("Ingrese el valor de incremento: "))


for numero in range(inicio, terminacion + 1, incremento):
    if numero % 7 == 0:
        print(f"{numero} es múltiplo de 7")
    else:
        print(numero)