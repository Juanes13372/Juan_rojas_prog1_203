
dias = int(input("Introduce el número de días del año: "))


if 1 <= dias <= 31:
    print("El mes es Enero")
elif 32 <= dias <= 59:
    print("El mes es Febrero")
elif 60 <= dias <= 90:
    print("El mes es Marzo")
elif 91 <= dias <= 120:
    print("El mes es Abril")
elif 121 <= dias <= 151:
    print("El mes es Mayo")
elif 152 <= dias <= 181:
    print("El mes es Junio")
elif 182 <= dias <= 212:
    print("El mes es Julio")
elif 213 <= dias <= 243:
    print("El mes es Agosto")
elif 244 <= dias <= 273:
    print("El mes es Septiembre")
elif 274 <= dias <= 304:
    print("El mes es Octubre")
elif 305 <= dias <= 334:
    print("El mes es Noviembre")
elif 335 <= dias <= 365:
    print("El mes es Diciembre")
else:
    print("Número de días fuera de rango")
