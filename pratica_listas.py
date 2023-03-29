# Criando uma lista de 1 a 1000000 e pegando o valor minimo, maximo e a soma dos valores da lista
"""
lista = []
for i in range(1,10000001, 1):
    lista.append(i)
print(lista)
minimo = min(lista)
maximo = max(lista)
soma = sum(lista)
print(minimo)
print(maximo)
print(soma)
"""

# Ímpares entre 1 e 20
for i in range(1, 20, 2):
    print(i)
print("\n")

# Múltiplos de 3 de 0 a 30
n = 3
for i in range(0, 31, 1):
    mult = i*3
    print(mult)
print("\n")

# Lista do cubo dos números de 1 a 10
lista_cubo = []
for i in range (1, 11, 1):
    cubo = i**3
    lista_cubo.append(cubo)
print(lista_cubo)
print("\n")


# Lista do cubo dos números de 1 a 10 com list comprehension

cubo_comprehension = [i**3 for i in range(1, 11)]
print("Usando List Comprehension")
print(cubo_comprehension)
print("\n")

print("Os três primeiros itens da lista são")
print(cubo_comprehension[:3])
print("\n")

# Cópia de listaa
meus_carros = ['Fiat Strada', 'D-20', 'Hilux']
seus_carros = meus_carros[:]
print(seus_carros)
meus_carros.append("RAM")
seus_carros.append("S-10")
print(meus_carros)
print(seus_carros)
for i in meus_carros:
    print(i)
print("\n")
for i in seus_carros:
    print(i)
print("\n")


# Trabalhando com Tuplas

lanches = ('Coxinha', 'Pizza', 'Pastel', 'Picolé', 'Sorvete')
for i in lanches:
    print(i)
print('\n')
# sobrescrevendo a tupla
lanches = ('Coxinha', 'Pizza', 'Pastel', 'Cachorro-quente', 'Enroladinho')
for i in lanches:
    print(i)
print("\n")


# Teste condicional com função lower
""""
nome = 'Eduardo'
nome1 = input("Digite um nome\n")

if nome.lower() == nome1:
    print("TRUE")
else:
    print("FALSE")

print("\n")
"""

# Procura uma letra na lista e retorna true ou false
lista = ['a', 'e', 'i', 'o', 'u']

if 'b' in lista:
    print("TRUE")
else:
    print("FALSE")
print("\n")

# Teste pra verificar se um item não está na lista
lista = ['a', 'e', 'i', 'o', 'u']

if 'b' not in lista:
    print("TRUE")
else:
    print("FALSE")
print("\n")


# Uso de instruções IF
usuario_cadastrado = ['admin', 'Francisco', 'Maria']
lista_usuario = []
#lista_usuario = ['admin', 'Paulo', 'Francisco', 'Maria', 'Joana']
if lista_usuario == '':
    for usuario in lista_usuario :
        if usuario == 'admin':
            print("Olá", usuario, "gostaria de ver um relatório de status?\n")
        else:
            print("Olá", usuario, "login feito com sucesso\n")
else:
    print("Precisamos adicionar usuários\n")

cadastro = input("Digite um nome de Usuário\n")
while cadastro in usuario_cadastrado:
    print("Usuário Inválido\n")
    cadastro = input("Digite um nome de Usuário\n")
while cadastro not in usuario_cadastrado:
    usuario_cadastrado.append(cadastro)
    print(usuario_cadastrado)
    print("Usuário cadastrado com Sucesso!!")
print("\n")
novo_cadastro = input("Digite um novo nome de Usuário\n")
if novo_cadastro in usuario_cadastrado:
    print("Usuário Inválido\n")
else:
    usuario_cadastrado.append(novo_cadastro)
print("Usuário cadastrado com sucesso!!\n")
print(usuario_cadastrado)
