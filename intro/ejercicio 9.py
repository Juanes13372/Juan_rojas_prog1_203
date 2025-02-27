
dia_presente = int(input("Ingrese el día actual:"))
mes_presente = int(input("Ingrese el mes actual:"))
año_presente = int(input("Ingrese el año actual:"))

dia = int(input("Ingrese el día:"))
mes = int(input("Ingrese el mes:"))
año = int(input("Ingrese el año:"))

if año_presente > año:
    print("Esa fecha ya pasó.")
elif año_presente < año:
    print("La fecha que ingresaste es del futuro.")
else:
    if mes_presente > mes:
        print("Esa fecha ya pasó.")
    elif mes_presente < mes:
        print("La fecha que ingresaste es del futuro.")
    else:
        if dia_presente > dia:
            print("Esa fecha ya pasó.")
        elif dia_presente < dia:
            print("La fecha que ingresaste es del futuro.")
        else:
            print("Es la fecha actual.")

