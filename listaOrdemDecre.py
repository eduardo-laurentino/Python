lista = [1, 2, 3, 4, 5]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim-1):
        if lista[x] < lista[x+1]: # Apenas a condição de verificação foi alterada
            trocou = True
            temp = lista[x]
            lista[x] = lista[x+1]
            lista[x+1] = temp
            #print(temp)
            #print(lista[x])
            #print(lista)
            x += 1
    if not trocou:
        break
    fim -= 1
for i in lista:
    print(i)