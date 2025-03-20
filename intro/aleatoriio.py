import random
cantidad=random.randint(1,15)
vector=[]
for i in range (cantidad):
    num=random.randint(1,100)
    vector.append(num)

print(vector) 
print(len(vector))
pares=[]
impares=[]

for i in range(len(vector)):
    if i%2==0:
        pares.append(vector[i])
    else:
         impares.append(vector[i])
    
print(f"los numeros pares son{pares}")
print(f"los numero son impares{impares}")
spar=0
for x in vector:
    if x %2==0


