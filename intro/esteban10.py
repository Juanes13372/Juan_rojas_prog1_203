
hora = input("Ingrese la hora en formato hh:mm:ss (hora militar, 24 horas): ")


horas = int(hora[0:2])
minutos = int(hora[3:5])
segundos = int(hora[6:8])
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
