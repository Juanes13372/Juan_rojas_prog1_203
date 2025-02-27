sg = int(input("Ingrese la cantidad de segundos: "))
if sg >= 3600:
    h = sg // 3600
    sg = sg - (h * 3600)
    print(f"{h} hora")

if sg >= 60:
    mn = sg // 60
    sg = sg - (mn * 60)
    print(f"{mn} minuto")

if sg > 0:
    print(f"{sg} segundo")
