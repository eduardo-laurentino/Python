carro = input("Qual carro deseja alugar?\n")
mensagem = "Deixe me ver se consigo este carro para você"
print(mensagem)
print("\n")


jantar = input("Quntas pessoas vão jantar com você?\n")
jantar = int(jantar)
if jantar > 8:
    print("Aguardem uma mesa")
else:
    print("Sua mesa está pronta")
print("\n")


# Deixando o usuário decidir quando quer sair do programa
entrada = "Digite um número ou QUIT para sair !!\n"
mensagem = ""
while mensagem != 'quit':
    mensagem = input(entrada)
    print(mensagem)
print("\n")

# Controlar se o programa deve ou não continuar executando com variável flag
ativo = True
while ativo:
    mensagem = input("Digite algo ou QUIT para sair!\n")
    if mensagem == 'quit':
        ativo = False
    else:
        print(mensagem)
print("\n")

# Usando BREAK para sair de um laço
cidades = ("Quais cidades você já visitou?\n Ou digite QUIT para sair:\n")
while True:
    cidade = input()
    if cidade == 'quit':
        break
    else:
        print(cidades)
    print("\n")

print("\n")

# Usando continue em um laço for
n = 0
while n < 10:
    n+=1
    if n % 2 == 0:
        print(n)
        continue
print("\n")


pedido = True
while pedido:
    mensagem = input("Informe um ingrediente\n")
    print("Você adicionou", mensagem, "a sua pizza\n" )
    if mensagem == 'quit':
        pedido = False
        print("Você saiu!\n")
print("\n")


idade = input("\nDigite a sua Idade ou QUIT para sair:\n")
if idade == 'quit':
    print("Você saiu!:\n")
else:
    while idade != 'quit':
        if int(idade) < 3:
            print("Entrada gratuita")
            break
        elif int(idade) >= 3 and int(idade) <= 12:
            print("O ingresso = $ 10.00")
            break
        else:
            print("O ingresso = $ 15.00")
            break
print("\n")


# Criando um dicionário e retornando um par chave-valor
usr0 = {
    'nome' : 'Eduardo',
    'primeiro_sobrenome' : 'Laurentino',
    'segundo_sobrenome' : 'Silva'
}
for key, valor in usr0.items():
    print("\nKey:", key, "\nvalue:", valor)
print("\n")


# Transferindo itens de uma lista para outra

usuario = ['Eduardo', 'Paulo', 'Maria', 'Francisco']
usuario_confirmado = []
while usuario:
    usuario_atual = usuario.pop()
    usuario_confirmado.append(usuario_atual)
for usuarios_confirmados in usuario_confirmado:
    print(usuarios_confirmados)
print("\n")


# Removendo ocorrências em listas

lista_animais = ['vaca', 'cavalo', 'bezerro', 'ovelha','vaca', 'cavalo', 'bezerro', 'ovelha', 'vaca', 'cavalo', 'bezerro', 'ovelha']

while 'vaca' in lista_animais:
    lista_animais.remove('vaca')
print(lista_animais)

# Preenchendo um dicionário com dados de entrada do usuário

resultado = {}
aux = True
while aux:
    nome = input("Qual seu nome?\n")
    resposta = input("Que lugar você gostaria de visitar um dia\n")
    resultado[nome] = resposta
    continua = input("Digite YES para continuar respondendo a enquete e NO para sair\n")
    if continua == 'no':
        aux = False
print("\n===== RESULTADOS =====\n")
for nome, resposta in resultado.items():
    print(nome + " : " + resposta)
