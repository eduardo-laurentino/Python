def geraTerceiraLista():
    primeira = []
    segunda = []
    while True:
        e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
        if e == 0:
            break
        primeira.append(e)
    while True:
        e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
        if e == 0:
            break
        segunda.append(e)
    terceira = primeira[:] # Copia os elementos da primeira lista
    terceira.extend(segunda)
    x = 0
    while x < len(terceira):
        print(f"{x}: {terceira[x]}")
        x = x + 1


def listaSemRepeticao():
    primeira = []
    segunda = []
    while True:
        e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
        if e == 0:
            break
        primeira.append(e)
    while True:
        e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
        if e == 0:
            break
        segunda.append(e)
    terceira = []


    i = 0
    terceira = []
    while i < len(primeira):
        terceira.append(primeira[i])
        terceira.append(segunda[i])
        i+=1
    terceira.sort()

    x = 0
    quarta = []
    while x < len(terceira):
        if terceira[x] in quarta:
            break
        else:
            quarta.append(x)
        x += 1
    
    x = 0
    while x < len(quarta):
        print(f"{x}: {quarta[x]}")
        x = x + 1

#geraTerceiraLista()
listaSemRepeticao()