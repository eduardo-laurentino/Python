# Trabalhando com dicionários


pessoa = {
    'nome' : 'Eduardo',
    'sobrenome' : 'Laurentino',
    'idade' : 22,
    'cidade' : 'Caxias'
}
print(pessoa)

# dicionário de números favoritos

numeros_favoritos = {
    'Maria' : 3,
    'Ana' : 7,
    'Mariana' : 12,
    'João' : 21,
    'Felipe' : 50,
}
print("Maria = ", numeros_favoritos['Maria'])
print("Ana = ",numeros_favoritos['Ana'])
print("Mariana = ", numeros_favoritos['Mariana'])
print("João = ", numeros_favoritos['João'])
print("Felipe = ", numeros_favoritos['Felipe'])



# Glossário usando dicionários
palavras = {
    'Int' : 'Inicializa um número inteiro',
    'If' :  'Operador relacional',
    'While' : 'Operador condicional',
    'Print' : 'Exibe algo  na tela',
    'Append' : 'Insere dados em uma lista'
}
print('Int = ', palavras['Int'])
print("\n")
print('If = ', palavras['If'])
print("\n")
print('While = ', palavras['While'])
print("\n")
print('Print = ', palavras['Print'])
print("\n")
print('Append = ', palavras['Append'])
print("\n")

# Percorrendo dicionários com laços for
palavras = {
    'Int' : 'Inicializa um número inteiro',
    'If' :  'Operador relacional',
    'While' : 'Operador condicional',
    'Print' : 'Exibe algo  na tela',
    'Append' : 'Insere dados em uma lista',
    'Pop' : 'Apaga todos os itens de uma lista',
    'Len' : 'Retorna o comprimento de uma lista',
    'Del' : 'Apaga registros'
}

for chave, valor in palavras.items():
    print(chave, valor)
print("\n")



rios = {
    'Nilo' : 'Egito',
    'São francisco' : 'Brasil',
    'Parnaíba' : 'Brasil'
}
for i in rios:
    if i == 'Nilo':
        print(i, "Corre pelo Egito\n")
    if i == 'São francisco' :
        print(i, "Corre pelo Brasil\n")
    if i == 'Parnaíba':
        print(i, "Corre pelo Brasil\n")

for chave, valor in rios.items():
    print(chave, valor)
print("\n")

lista_enquete = ['Mateus', 'André', 'Márcio', 'Pedro', 'Alan']
respondeu_enquete = []
print("Pessoas que devem responder da enquete\n")
print(lista_enquete)
print("\n")
for i in lista_enquete:
    if i in respondeu_enquete:
        print("Obrigado por responderem a enquete")
    else:
        print(i, "Responda a enquete por favor")
print("\n")


# Informações aninhadas com dicionário
# Dicionários dentro de listas
Carro1 = {'modelo' : 'toyota', 'nome' : 'jhilux', 'cor' : 'vermelha'}
carro2 = {'modelo' : 'chevrolet', 'nome' : 's-10', 'cor' : 'branca'}
Carro3 = {'modelo' : 'ford', 'nome' : 'ranger', 'cor' : 'azul'}
carro4 = {'modelo' : 'wolksvagen' , 'nome' : 'amarok', 'cor' : 'preta'}
carro5 = {'modelo' : 'nissan', 'nome' : 'frontier', 'cor' : 'prata'}

carros = [Carro1, carro2, Carro3, carro4, carro5]
for carro in carros:
    print(carro)
print("\n")
# Exibe até onde quer exibir carros
for carro in carros [:3]:
    print(carro)
print("\n")



# Listas dentro de dicionários
linguagens_favoritas = {
    'Marcos' : ['php', 'dart', 'c'],
    'Matheus' : ['java', 'c', 'python' ],
    'Eduardo' : ['c', 'rust', 'python'],
    'Maria' : ['html', 'css', 'javascript']
}
for nome, valor in linguagens_favoritas.items():
    print("\n", nome.title())
    for linguagem in valor:
        print("\t", linguagem.title())
    print("\n")


# Dicionário em um dicionário

usuario = {
    'usuario1' : {
        'nome' : 'Eduardo',
        'sobrenome' : 'Laurentino',
        'localidade' : 'Caxias'
    },
    
    'usuario2' : {
        'nome' : 'Maria',
        'sobrenome' : 'Sousa',
        'localidade' : 'Passagem Franca'
    },

    'usuario3' : {
        'nome' : 'Ana',
        'sobrenome' : 'Silva',
        'localidade' : 'Rio de Janeiro'
    }
}

# Dicionário aninhados com chaves iguais não é complicado de percorrer
for users, dados in usuario.items():
    nome_completo = dados['nome'] + " " + dados['sobrenome'] + " -> " + dados['localidade']
    print(users, ':', nome_completo)
print("\n")

# Criando um novo dicionário usuário
usuario1 = {
    'nome_completo' : 'Eduardo Laurentino',
    'idade' : '22 anos',
    'localidade' : 'Caxias - MA'
}
usuario2 = {
    'nome_completo' : 'Mariana Silva',
    'idade' : '25 anos',
    'localidade' : 'Rio de Janeiro - RJ'
}
lista_usuario = [usuario1, usuario2]
for dados in lista_usuario:
    print(dados)
print("\n")

# Criando dicionário animais de estimação

cachorro = {
    'nome' : 'Dog',
    'sexo' : 'Macho',
    'raça' : 'budog',
    'idade' : '3 anos',
    'localidade' : 'São Paulo - SP',
    'nome_dono' : 'Jorge'
}

gato = {
    'nome' : 'Miau',
    'sexo' : 'Macho',
    'raça' : 'Siamês',
    'idade' : '2 anos',
    'localidade' : 'Brasilia - DF',
    'nome_dono' : 'Milena'
}
lista_animais = [cachorro, gato]
for dados in lista_animais:
    print(dados)
print("\n")

# Dicionário lugares favoritos
lugares_favoritos = {
    'Jaqueline' : ['Nova Iorque', 'Colônia', 'Pequi'],
    'Natália' : ['Lençóis Maranhenses', 'Poço Azul', 'Pantanal'],
    'Joyce' : ['Cataratas do Iguaçú', 'Maldivas', 'Disney']
}
# Exibe somente dados fora do dicionário e da lista
for nome, dados in lugares_favoritos.items():
    print("\n", nome)
    for dado in dados:
        print("\t", dado.title())
print("\n")


# Criando um dicionário dentro de outro dicionário

cidades = {
    'Passagem Franca' : {
        'pais' : 'Brasil',
        'estado' : 'Maranhão',
        'população' : '20 mil habitantes'
    },
    'Lagoa do Mato' : {
        'pais' : 'Brasil',
        'estado' : 'Maranhão',
        'população' : '10 mil habitantes'
    },
    'Buriti Bravo' :{
    'pais': 'Brasil',
    'estado' : 'Maranhão',
    'população' : '25 mil habitantes'
    }
}
for city, dados in cidades.items():
    informacao = dados['pais']+ " " + dados['estado']+ " " + dados['população']
    print(city, informacao)

# Dicionário de objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
pessoa1 = Pessoa("Eduardo", 23)
pessoa2 = Pessoa("Bob", 25)
pessoa3 = Pessoa("Carol", 35)

dictPessoas = {
    'pessoa1':pessoa1,
    'pessoa2':pessoa2,
    'pessoa3':pessoa3
}

print(dictPessoas['pessoa2'].nome)