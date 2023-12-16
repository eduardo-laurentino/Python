from time import sleep
from random import randint
import calendar
from gtts import gTTS
from playsound import playsound
import os
from barcode import EAN13
from barcode.writer import ImageWriter  # para salvar em png
import qrcode
import emoji
import serial
import requests
from datetime import datetime
import pywhatkit


def calculaValorCompra():
    ValorApagar = 0
    while True:
        codigo = int(input("Código da mercadoria (0 para sair): "))
        preco = 0
        if codigo == 0:
            break
        elif codigo == 1:
            preco = 0.50
        elif codigo == 2:
            preco = 1.00
        elif codigo == 3:
            preco = 4.00
        elif codigo == 5:
            preco = 7.00
        elif codigo == 9:
            preco = 8.00
        else:
            print("Código inválido!")
        if preco != 0:
            quantidade = int(input("Quantidade: "))
            ValorApagar = ValorApagar + (preco * quantidade)
    print(f"Total a pagar R${ValorApagar:.2f}")


def funcaoSleep():
    # faz uma contagem regressiva
    for i in range(0, 11, 1):
        print(i, end=' ', flush=True)
        sleep(1)


def sorteio():
    # Sorteia números aleatórios
    aposta = set()
    numeros = 0
    while numeros < 15:
        aposta.add(randint(1, 25))
        numeros = len(aposta)
    print(aposta)


def testeStrings():
    frase = 'Eduardo Laurentino da Silva'

    print(frase[3])
    print(frase[3:13])
    print(frase[:13])
    print(frase[13:])
    print(frase[:13:2])
    print(frase.upper().count('a'))
    print(len(frase))
    print(len(frase.strip()))
    print(frase.find('Laurentino'))
    print('Eduardo' in frase)
    print(frase.find('laurentino'))
    print(frase.lower().find('laurentino'))
    print(frase.count(' '))
    print("\033[1;32;41mOlá, Mundo!\033[m")


def encontraNomeString():
    # Verifique se a segunda ocorre dentro da primeira e imprima a posição de início
    primeira = input("Digite a primeira string: ")
    segunda = input("Digite a segunda string: ")
    posição = primeira.find(segunda)
    # O método "find" retorna a posição de inicio da substring na string.
    if posição == -1:
        print(f"'{segunda}' não encontrada em '{primeira}'")
    else:
        print(f"{segunda} encontrada! Inicia na posição {posição} de {primeira}")


def substituiCaractereString():
    # Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira. 1ª string: AATTCGAA 2ª string: TG 3ª string: AC Resultado: AAAACCAA

    primeira = input("Digite a primeira string: ")
    segunda = input("Digite a segunda string: ")
    terceira = input("Digite a terceira string: ")
    if len(segunda) == len(terceira):
        resultado = ""
        for letra in primeira:
            posição = segunda.find(letra)
            if posição != -1:
                resultado += terceira[posição]
            else:
                resultado += letra
        if resultado == "":
            print("Todos os caracteres foram removidos.")
        else:
            print(f"Os caracteres {segunda} foram substituidos por "
                  f"{terceira} em {primeira}, gerando: {resultado}")
    else:
        print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")


def tabuada():
    while True:
        print("""
        Menu
        ---------
        1 - Adição
        2 - Subtração
        3 - Divisão
        4 - Multiplicação
        5 - Sair
        """)
        opção = int(input("Escolha uma opção:"))
        if opção == 5:
            break
        elif opção >= 1 and opção < 5:
            n = int(input("Tabuada de:"))
            x = 1
            while x <= 10:
                if opção == 1:
                    print(f"{n} + {x} = {n + x}")
                elif opção == 2:
                    print(f"{n} - {x} = {n - x}")
                elif opção == 3:
                    print(f"{n} / {x} = {n / x:5.4f}")
                elif opção == 4:
                    print(f"{n} x {x} = {n * x}")
                x = x + 1
        else:
            print("Opção inválida!")


def quebraSenha():
    senha = input("Digite a senha que você quer encontrar: ")
    combinacoes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                   'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '*', '(', ')', '{', '}', '[', ']', '^', '~', '?', '/', '&']

    achou = ""
    while (achou != senha):
        achou = ""
        for caractere in senha:
            achouCaractere = combinacoes[randint(0, 52)]
            achou = str(achouCaractere)+str(achou)
        print(achou)


def geraCalendario():
    ano = 2023
    mes = 3
    # Gera um calendário
    calendario = calendar.month(ano, mes)
    print(calendario)


def operacoesMatematicas():
    a = float(input("Primeiro número:"))
    b = float(input("Segundo número:"))
    operação = input("Digite a operação a realizar (+,-,* ou /):")
    if operação == "+":
        resultado = a + b
    elif operação == "-":
        resultado = a - b
    elif operação == "*":
        resultado = a * b
    elif operação == "/":
        resultado = a / b
    else:
        print("Operação inválida!")
        resultado = 0
    print("Resultado: ", resultado)


def geraAudio():
    audio = 'audio.mp3'
    language = 'pt-br'
    # Converte a frase para áudio
    sp = gTTS(
        text='Estou aprendendo Python',
        lang=language)
    sp.save(audio)
    playsound(audio)


def palavraSecreta():
    palavra_secreta = "eduardo"
    letras_acertadas = ""
    tentativas = 0

    while True:
        letra_digitada = input("Digite uma letra: ")
        tentativas += 1
        if len(letra_digitada) > 1:
            print("Digite apenas uma letra.")
            continue

        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada

        palavra_formada = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += "*"
        print("Palavra formada ", palavra_formada)
        if palavra_formada == palavra_secreta:
            os.system("clear")
            print("VOCÊ GANHOU!! PARABÉNS!")
            print("A palavra era: ", palavra_secreta)
            print("Tentativas: ", tentativas)
            letras_acertadas = ""
            tentativas = 0


def geraCodigoBarras():
    codigos_produtos = {
        "Feijao": "551746511111",
        "Arroz": "665789011111",
        "Macarrao": "665887111111",
        "Azeite": "998556211111"}

    for produto in codigos_produtos:
        # writer para salvar em png
        codigo_barra = EAN13(codigos_produtos[produto], writer=ImageWriter())
        codigo_barra.save(f"{produto}_codigo")


def geraQrCode():
    # Crie um objeto QRCode com o texto que você deseja codificar
    qr = qrcode.QRCode(
        version=1,  # Versão do QR Code (1 a 40)
        # Nível de correção de erros (L, M, Q ou H)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Tamanho dos blocos (pixels)
        border=4,  # Tamanho da borda (blocos)
    )

    # Adicione os dados que você deseja codificar
    # Pode ser um URL, texto, etc.
    texto = "https://monitoramentopiscicultura.eduardolaurenti.repl.co/dados"
    qr.add_data(texto)
    qr.make(fit=True)

    # Crie uma imagem do QR Code usando a biblioteca PIL
    img = qr.make_image(fill_color="black", back_color="white")

    # Salve a imagem em um arquivo
    img.save("qrcode.png")


def achouPrimeiro():
    l = [15, 7, 27, 39]
    p = int(input("Digite o valor a procurar (p): "))
    s = int(input("Digite o outro valor a procurar (v): "))
    x = 0
    achouP = False
    achouV = False
    primeiro = 0
    while x < len(l):
        if l[x] == p:
            achouP = True
            if not achouV:
                primeiro = 1
        if l[x] == s:
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


def perguntaResposta():
    perguntas = [
        {
            'Pergunta': 'Quanto é 2 + 2?',
            'Opções': [1, 3, 4, 5],
            'Resposta': 4
        },
        {
            'Pergunta': 'Quanto é 3 - 3?',
            'Opções': [1, 3, 0, 5],
            'Resposta': 0
        },
        {
            'Pergunta': 'Quanto é 5 * 5?',
            'Opções': [25, 55, 10, 51],
            'Resposta': 25
        },
        {
            'Pergunta': 'Quanto é 10 / 2?',
            'Opções': [2, 3, 4, 5],
            'Resposta': 5
        },
    ]

    acertos = 0
    for pergunta in perguntas:
        print('Pergunta: ', pergunta['Pergunta'])
        print()
        for i, opcao in enumerate(pergunta['Opções']):
            print(f'{i}) ', opcao)
        print()
        escolha_opcao = input("Escolha uma opção: ")
        acertou = False
        escolha_int = None
        qtd_opcoes = len(pergunta['Opções'])

        if escolha_opcao.isdigit():
            escolha_int = int(escolha_opcao)

        if escolha_int is not None:
            if escolha_int >= 0 and escolha_int < qtd_opcoes:
                if pergunta['Opções'][escolha_int] == pergunta['Resposta']:
                    acertou = True
        if acertou:
            acertos += 1
            print("Acertou!", emoji.emojize(':thumbs_up:'))
        else:
            print("Errou!", emoji.emojize(':cross_mark:'))
        print()

    print(f"Voçê acertou {acertos} de {len(perguntas)} perguntas")

def ArduinoPython():
    arduino = serial.Serial("/dev/ttyACM0", 9600)
    while True:
        linha = str(arduino.readline())
        linha_teste = linha[2:-15]
        print(linha_teste, "°C")
        arduino.close()

def contPalavras():
    filename = 'palavra.txt'
    soma = 0
    with open(filename) as file_object:
        lines = file_object.readlines()
        for i in lines:
            qtd = i.lower().count('uma')
            #print(i)
            soma += qtd
        print(soma)

def estoque():
    estoque = {"tomate": [1000, 2.30],
            "alface": [500, 0.45],
            "batata": [2001, 1.20],
            "feijão": [100, 1.50]}
    total = 0
    print("\n\n ---------- Vendas: -----------\n\n")
    print("TOMATE\nALFACE\nBATATA\nFEIJÃO\n")
    while True:
        produto = input("Nome do produto (FIM para sair):").lower()
        if produto == "fim":
            break
        if produto in estoque:
            quantidade = int(input("Quantidade:"))
            if quantidade <= estoque[produto][0]:
                preço = estoque[produto][1]
                custo = preço * quantidade
                print(f"{produto}: {quantidade:.2f} x {preço:.2f} = {custo:.2f}")
                estoque[produto][0] -= quantidade
                total += custo
            else:
                print("Quantidade solicitada não disponível")
        else:
            print("Nome de produto inválido")
            print(f" Custo total: {total:.2f}\n")
            print("Estoque:\n")
            for chave, dados in estoque.items():
                print("Descrição: ", chave)
                print("Quantidade: ", dados[0])
                print(f"Preço: {dados[1]:.2f}\n")


def cotacaoMoedas():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()
    print(requisicao_dic)

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")

def enviaZap():
    pywhatkit.sendwhatmsg_instantly('+55 número', 'Olá')


def PesquisaSequencial():
    # Exemplo de uso:
    lista = [3, 7, 1, 9, 4, 6, 8]
    alvo = 4
    for i in range(len(lista)):
        if lista[i] == alvo:
            print(f'O elemento {alvo} foi encontrado no índice {i}.')
            exit()
    print(f'O elemento {alvo} não foi encontrado na lista.')

def pesquisaBinaria():
    lista = [1, 3, 4, 6, 7, 8, 9]
    alvo = 4
    esquerda = 0
    direita = len(lista) - 1
    print("Direita = ", direita)

    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # Calcula o índice do meio

        if lista[meio] == alvo:
            print(f'O elemento {alvo} foi encontrado no índice {meio}.')
            return meio  # Retorna o índice onde o elemento foi encontrado
        elif lista[meio] < alvo:
            esquerda = meio + 1  # O alvo está na metade direita
        else:
            direita = meio - 1  # O alvo está na metade esquerda

    print(f'O elemento {alvo} não foi encontrado na lista.')


#calculaValorCompra()
#funcaoSleep()
#sorteio()
#testeStrings()
#encontraNomeString()
#substituiCaractereString()
#tabuada()
#quebraSenha()
#geraCalendario()
#operacoesMatematicas()
#geraAudio()
#palavraSecreta()
#geraCodigoBarras()
#geraQrCode()
#achouPrimeiro()
#perguntaResposta()
#ArduinoPython()
#contPalavras()
#estoque()
#cotacaoMoedas()
#enviaZap()
#PesquisaSequencial()
#pesquisaBinaria()