
horas = int(input("Ingrese la hora (horas): "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

segundos += 1

if segundos == 60:
    segundos = 0
    minutos += 1
    
    if minutos == 60:
        minutos = 0
        horas += 1
        
        if horas == 24:
            horas = 0


print(f"La hora un segundo después es: {horas:02}:{minutos:02}:{segundos:02}")
