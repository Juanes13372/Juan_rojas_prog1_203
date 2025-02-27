num= int(input("ingrese un numero:"))
if num<10:
    print("el numero tiene 1 cifra")
elif num<100:
    print("el numero tiene 2 cifras")
elif num< 1000:
    print("el numero tiene 3 cifras")
elif num<10000:
    print("el numero tiene 4 cifras") 
else:
    print("el numero excede a mas de 4 cifras")