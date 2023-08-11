L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar (p): "))
s = int(input("Digite o outro valor a procurar (v): "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[x] == s:
        achouV = True
        if not achouP:
            primeiro = 2
    x += 1
if achouP:
    print(f"p: {p} encontrado")
else:
    print(f"p: {p} não encontrado")
if achouV:
    print(f"v: {s} encontrado")
else:
    print(f"v: {s} não encontrado")
if primeiro == 1:
    print("O Primeiro foi achado antes do Segundo")
elif primeiro == 2:
    print("O Segundo foi achado antes do Primeiro")