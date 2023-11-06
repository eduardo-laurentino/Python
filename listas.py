# Formas de criar uma lista
lista = []
lista2 = list()

# Lista de inteiros
listaInteiros = [1, 2, 3, 4, 5]
# Lista de strings
turismo = ['Lençóis Maranhenses', 'Pantanal', 'Serra da Capivara', 'Poço Azul', 'Mato Grosso do Sul']
# Lista de tips diferentes
variosTipos = ['Eduardo', 1, 2, 'Maria', 3, 4]
print(turismo)
print(variosTipos)
# Append adiciona elementos ao final da lista
listaInteiros.append(8)
print(listaInteiros)
# Insert adiciona o elemento em uma posição especifica
listaInteiros.insert(1, 3)
print(listaInteiros)
# Remove, remove um elemento com base no seu valor
listaInteiros.remove(8)
print(listaInteiros)
# Del remove um elemento com base no indice
del listaInteiros[3]
print(listaInteiros)
# Mostra a lista na ordem inversa
listaInteiros.reverse()
print(listaInteiros)
# Sorted ordena uma lista
print('\n')
print(sorted(turismo))
print('\n')
inverso = sorted(turismo)
inverso.sort(reverse = True)
print(inverso)
print('\n')
print(turismo)
turismo.reverse()
print(turismo)
turismo.reverse()
print(turismo)
print('\n')
turismo.sort()
print(turismo)
turismo.sort(reverse = True)
print(turismo)

tamanho = len(turismo)
print(tamanho)

nomes = ['Eduardo', 'Maria']
for nome in nomes:
    print("Olá, "+nome.title())



numeros = []
for valor in range (1, 11):
    numeros.append(valor**2)
print(numeros)

num = []
num = list(range(1, 6))
print(num)


# Usando list comprehension

print('\n')
print('Usando list comprehension')

digitos = [valor**2 for valor in range(1, 11)]
print(digitos)

listaDeLista = []
listaDeLista.append(listaInteiros)
listaDeLista.append(variosTipos)
print(listaDeLista)

print(listaDeLista[0][1])

print("Operação de conjuntos em listas")
l1 = [1, 2, 6, 8]
l2 = [3, 6, 8, 9]
print(f"Lista 1: {l1}")
print(f"Lista 2: {l2}")
conjunto_1 = set(l1)
conjunto_2 = set(l2)
# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)
# Conjuntos suportam o operador ^ que realiza a subtração simétrica.
# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
# A ^ B = A - B | B - A
print("Elementos não repetidos nas duas listas:", conjunto_1 ^
conjunto_2)
# Repetido:
print("Primeira lista, sem os elementos repetidos na segunda:",
conjunto_1 - conjunto_2)

lista_de_pessoas = [
    {"nome": "Alice", "idade": 30, "cidade": "Nova Iorque"},
    {"nome": "Bob", "idade": 25, "cidade": "Los Angeles"},
    {"nome": "Carol", "idade": 35, "cidade": "Chicago"}
]

# Acessa o primeiro dicionário da lista
print(lista_de_pessoas[0])
# Altera a idade da pessoa no primeiro dicionário
lista_de_pessoas[0]['idade'] = 10
print(lista_de_pessoas[0]['idade'])

# Listas de objetos 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
pessoa1 = Pessoa("Eduardo", 23)
pessoa2 = Pessoa("Bob", 25)
pessoa3 = Pessoa("Carol", 35)

pessoas = [pessoa1, pessoa2,pessoa3]
print(pessoas[1].nome, "\n", pessoas[1].cumprimentar())
