
minutos = int(input("Introduce los minutos de la llamada: "))

banderazo = 200

if minutos <= 3:
    costo_total = banderazo
else:
    minutos_adicionales = minutos - 3
    costo_total = banderazo + (minutos_adicionales * 50)

print("El costo total de la llamada es: ", costo_total)
