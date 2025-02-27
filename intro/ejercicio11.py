din = int(input("Ingrese la cantidad de dinero: "))
if din >= 50000:
    billetes50 = din // 50000
    din = din - (billetes50 * 50000)
    print(f"{billetes50} billetes de 50.000")

if din >= 20000:
    billetes20 = din // 20000
    din = din - (billetes20 * 20000)
    print(f"{billetes20} billete de 20.000")

if din >= 10000:
    billetes10 = din // 10000
    din = din - (billetes10 * 10000)
    print(f"{billetes10} billete de 10.000")

if din >= 5000:
    billetes5 = din // 5000
    din = din - (billetes5 * 5000)
    print(f"{billetes5} billete de 5.000")

if din >= 2000:
    billetes2 = din // 2000
    din = din - (billetes2 * 2000)
    print(f"{billetes2} billete de 2.000")

if din >= 1000:
    billetes1 = din // 1000
    din = din - (billetes1 * 1000)
    print(f"{billetes1} billete de 1.000")
