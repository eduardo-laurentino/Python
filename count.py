filename = 'palavra.txt'
soma = 0
with open(filename) as file_object:
    lines = file_object.readlines()
    for i in lines:
        qtd = i.lower().count('uma')
        #print(i)
        soma += qtd
    print(soma)
