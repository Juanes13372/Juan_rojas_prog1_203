n= int(input("ingresar numero"))
m= int(input("ingresar numero"))
o= int(input("ingresar numero"))
if n>m:
    if n<o:
        print(f"el numero del medio es:{n}")
    else:
        if m>o:
            print(f"el numero del medio es:{m}")
        else:
            print(f"el numero del medio es:{o}")
else:
    if n>o:
        print(f"el numero del medio es:{n}")
    else:
        if m<o:
            print(f"el numero del medio es:{m}")
        else:
            print(f"el numero del medio es:{o}")

