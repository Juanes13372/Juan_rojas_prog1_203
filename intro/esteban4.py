
nota = float(input("Introduce una nota entre 0 y 10: "))

if 0 <= nota <= 10:
    if 0 <= nota < 5:
        print("Insuficiente")
    elif 5 <= nota < 6:
        print("Suficiente")
    elif 6 <= nota < 8:
        print("Bien")
    elif 8 <= nota < 9:
        print("Excelente")
    else:
        print("Súper")
