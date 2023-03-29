# Criando a lista
lista_convidados = ['Maíra', 'Maria', 'Juliana', 'Ana', 'Alice', 'João', 'Paulo', 'Cícero']
msg = 'Olá,'
mensagem ='passando aqui para convidálo(a) para um jantar. Será sábado em minha residência'
a = 0
j = 0
k = 0
l = 0
for i in lista_convidados:
    # Percorrendo a lista
    convite = lista_convidados[a]
    # Passando uma mensagem para todos que estão na lista
    print(msg,convite, mensagem)
    # Contado que faz o laço que percorre a lista repetir
    a+=1
print("\n\n")
# Removendo pessoas da lista com o método POP
remover = lista_convidados.pop(2)
print(remover, "Não poderá participar do jantar")
print("\n")
for i in lista_convidados:
    # Percorre a nova lista depois de remover uma pessoa
    convite = lista_convidados[j]
    j+=1
    # Manda mensagem pra quem ainda tá na lista
    print(msg, convite, mensagem)
print("\n\n")
# Passa um aviso para todas as pessoas da lista
print('Encontrei uma mesa maior, portanto convidarei mais 3 pessoas')
print("\n")
# Atualizando a lista
lista_convidados.insert(0,'Marcos')
lista_convidados.insert(4,'Mateus')
lista_convidados.append('Jorge')
# Exibe a lista atualizada
print(lista_convidados)
print("\n")
for i in lista_convidados:
    # Percorrendo a lista
    convite = lista_convidados[k]
    # Exibindo uma mensagem para todos da lista
    print(msg,convite, mensagem)
    k+=1
print("\n")

print('Olá, venho trazer mais uma atualização sobre o jantar. Infelizmente a mesa não chegará a tempo. então só posso convidar duas pessoas')
msg_desculpa = 'Lamento informar que depois do ocorrido não posso manter o covite que lhe fiz. Desculpas'
msg_convidados = 'Conto com você para o jantar'
# Remove itens da lista até ela ficar vazia
while len(lista_convidados) != 0:
    # Método POP usado para remover intens do final da lista um por vez
    print(lista_convidados.pop(), msg_desculpa)
    # Verifica se a lista está vazia 
if len(lista_convidados) == 0:
    # Se lista estiver vazia insere novos itens com o método APPEND. inserindo sempre no final da lista 
    print("\n")
    lista_convidados.append('Ana') 
    lista_convidados.append('Maíra')
    print(lista_convidados)
    print("\n")
    # Percorrendo a lista
    for i in lista_convidados:
        # Método que percorre a lista
        convite = lista_convidados[l]
        # Exibe uma mensagem para quem ainda está na lista
        print(msg,convite, msg_convidados)
        l+=1

else:
    # É executado somente se a lista não estiver vazia e apaga todos os itens
    lista_convidados.pop()

while len(lista_convidados) != 0:
    del lista_convidados[0]
print(lista_convidados)
