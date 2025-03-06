import random
num=random.randint(1,100) 
print(num)
num2=1
cont=0
while num!=num2:
    num2=int(input("adivina el valor"))
    cont+=1
print(f"numero de intentos{cont}") 
