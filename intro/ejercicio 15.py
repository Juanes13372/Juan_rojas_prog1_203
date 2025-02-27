año = int(input("Ingrese año: "))
A = año % 19
B = año % 4
C = año % 7
D = (19 * A + 24) % 30
E = (2 * B + 4 * C + 6 * D + 5) % 7
N = 22 + D + E

if N > 31:
    print(f"La fecha de Pascua en el año {año} es el {N - 31} de abril.")
else:
    print(f"La fecha de Pascua en el año {año} es el {N} de marzo.")
