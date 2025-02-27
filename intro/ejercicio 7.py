x = int(input("Ingrese horas trabajadas: "))
if x > 40:
    m= ((x - 40) * 5000) +  (40 * 2600) 
    print(f"El salario es: {m}")
elif x <= 40:
    m = x * 2600
    print(f"El salario es: {m}")
else:
    print("horas no validas.")
