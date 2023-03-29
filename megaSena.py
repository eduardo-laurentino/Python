from random import randint
#Sorteia números aleatórios
aposta = set()
numeros = 0
while numeros < 6:
    aposta.add(randint(1, 60))
    numeros = len(aposta)
print(aposta)
