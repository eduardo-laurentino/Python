# Criando funções
def cumprimentar_usuario(nome):
    """Exibe uma saudação simples"""
    print("Olá " + nome.title())
cumprimentar_usuario("eduardo")
cumprimentar_usuario("sarah")


def mensagem():
    print("olá, estou aprendendo a usar funções em Python!")
mensagem()


def livros_favoritos(titulo):
    print("Um dos meus livros favoritos é " + titulo.title())
livros_favoritos("Curso intensivo de Python")

# função com argumentos pposicionais
def animal(tipo_animal, nome):
    print("Eu tenho um " + tipo_animal.title() + " e seu nome é : " + nome.title())
animal('cachorro', 'dog')


#função com argumentos nomeados
def animal(tipo_animal, nome):
    print("Eu tenho um " + tipo_animal.title() + " e seu nome é : " + nome.title())
animal(tipo_animal='cachorro', nome ='totó')

# Valores default
def animal(nome, tipo_animal = 'gato'):
    print("Eu tenho um " + tipo_animal.title() + " e seu nome é : " + nome.title())
animal(nome = 'totó')

def fazer_camisa(tamanho, mensagem):
    #return print("Tamanho da camisa = ", tamanho.title(), " Mensagem = ", mensagem.title())
    tam = tamanho + ' ' + mensagem
    return tam.title()


retorno = fazer_camisa('m', 'Olá!')
print("\n")
print(retorno)
print("\n")

# Deixando argumentos opcionais
def nome_completo(nome, primeiro_sobrenome, segundo_sobrenome = ' '):
    nome_todo = nome + ' ' + primeiro_sobrenome + ' ' + segundo_sobrenome
    return nome_todo.title()

retorna_nome = nome_completo('eduardo', 'laurentino')
print(retorna_nome)
print("\n")


# Retorna função com argumento opcional ou não
def nome_completo(nome, primeiro_sobrenome, segundo_sobrenome = ' '):
    if segundo_sobrenome:
        nome_todo = nome + ' ' + primeiro_sobrenome + ' ' + segundo_sobrenome
        return nome_todo.title()
    else:
        nome_todo = nome + ' ' + primeiro_sobrenome
        return nome_todo.title()

retorna_nome = nome_completo('eduardo', 'laurentino', 'silva')
print(retorna_nome)
print("\n")


# Funções que retornam dicionários

def dicionário(nome_pessoa, primeiro_sobrenome, anos = ''):
    pessoa = {
        'nome' : nome_pessoa.title(),
        'sobrenome' : primeiro_sobrenome.title()
        }
    if anos:
        pessoa['idade'] = anos
        return pessoa
    return pessoa
retorno = dicionário('eduardo', 'laurentino', '22')
print("\n")


# Função com entrada de dados do usuário

def pessoas(*args):
    while True:
        nome = input("Digite seu nome\n")
        sobrenome = input("Digite seu sobrenome\n")
        nome_completo = nome + ' ' + sobrenome
        print(nome_completo.title())
        sair = input("Se desejar sair digite QUIT\n")
        if sair == 'quit':
            print("Voçê saiu!\n")
            break
pessoas()


def nome_cidade(nome, pais):
    result = nome.title() + ', ' + pais.title()
    print(result)

nome_cidade('caxias', 'brasil')


def album(*args):
    ativo = True
    while ativo == True:
        nome_artista = input('Informe o nome do artista\n')
        titulo_album = input('Informe o nome do álbum\n')
        qtd_faixas = input("Informe a quantidade de faixas do álbum\n")
        album_artista = {
            'nome' : nome_artista.title(),
            'titulo' : titulo_album.title(),
            'faixas' : qtd_faixas
            }
        print(album_artista)
        sair = input("Digite QUIT se desejar sair\n")
        if sair == 'quit':
            print("Voçê saiu!\n")
            break
album()


# Usando lista em funções
def saudacao(nomes):
    print("Exibe uma saudação simples a cada usuário da lista\n")
    for name in nomes:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

nomes_pessoas = ['patricia', 'aline', 'lara', 'joão', 'paulo', 'ricardo', 'eduardo']
saudacao(nomes_pessoas)
print("\n")



"""
O çodigo a seguir tem um pequeno problema que não interfere na execução e no resultado esperado da função.
O problema é que ao passarmos a lista_designs para lista_a fabricar a lista_designs é perdida.
Podemos usar um método que não altera a lista e apenas copia ela. Passamos ele na chamada da função assim:
grafica(lista_designs[:])
Esse método só é usado quando somos obrigados a manter a lista original intacta

"""
def grafica(lista_designs):
    lista_fabricados = []
# Percorre a lista e transfere os produtos que não foram fabricados para a lista de produtos que vão ser fabricados
    while lista_designs:
        lista_fabricar = lista_designs.pop()
        print("Modelo para fabricação = ", lista_fabricar.title())
# Coloca os produtos que foram fabricados na lista de produtos fabricados
        lista_fabricados.append(lista_fabricar.title())
    print("===== Os seguintes modelos foram impressos =====")
# Percorre a lista de produtos fabricados e exibe cada produto
    for modelo_impresso in lista_fabricados:
        print(modelo_impresso.title())
    print(lista)

# Chamada da função passando uma lista como parâmetro
lista = ['capinha iphone', 'pingente de robô', 'bola']
grafica(lista[:])
print("\n")

# Funções com o parâmetro *toppings ou *args. Essa função recebe uma tupla com 1 ou mais valores

def pizzas(tamanho, *args):
    print(" ===== Lista de ingredientes ===== \n")
    print("Fazendo uma pizza de ", tamanho, " polegadas com as seguintes coberturas\n")
    for ingredientes in args:
        print("-",ingredientes.title())

pizzas('16', 'cogumelos')
pizzas('12', 'calabresa', 'pimentão verde', 'queijo')
print("\n")

# Inserido dados em um dicionário que já tinha informações inicialmente
# O parâmetro **informacao_usuario permite inserir quantos pares chave-valor desejarmos e organiza no dicionário
def perfil_usuario(nome, sobrenome, **informacao_usuario):
    perfil = {
        'nome_perfil': nome,
        'sobrenome_perfil': sobrenome
    }
    for chave, valor in informacao_usuario.items():
        perfil[chave] = valor
    return perfil

users_perfil = perfil_usuario('eduardo', 'laurentino', sexo = 'masculino', pais = 'brasil')
print(users_perfil)


