import json
from random import randint
import smtplib
import email.message


def menu():
    menu = True
    while menu:
        print("""
        =============================
        1 - CRIAR CONTA 
        2 - LOGIN
        3 - ESQUECEU A SENHA?
        =============================

        """)
        op = int(input("DIGITE UMA OPÇÃO: "))
        while op:
            if op == 1:
                criarConta()
                break
            elif op == 2:
                login()
                break
            elif op == 3:
                recuperarSenha()
                break


def criarConta():
    print("----- CRIANDO CONTA -----")
    usuario = str(input("Digite seu nome: "))
    email = str(input("Digite seu email: "))
    senha = str(input("Digite sua senha: "))
    codigo = str(input("Digite o código do seu equipamento: "))
    dados = {
        'usuario': usuario,
        'email': email,
        'senha': senha,
        'codigo': codigo
    }

    with open('usuario.json', 'w') as arquivo:
        json.dump(dados, arquivo)


def login():
    print("------ LOGIN -----")
    emailDigitado = str(input("Digite seu Email: "))
    senhaDigitada = str(input("Digite sua Senha: "))
    with open('usuario.json', 'r') as arquivo:
        dadosUsuario = json.load(arquivo)
        if emailDigitado == dadosUsuario['email'] and senhaDigitada == dadosUsuario['senha']:
            print("Login feito com sucesso!")
        else:
            print("Dados Inválidos!")


def recuperarSenha():
    resposta = str(input("Deseja recuperar senha? [S/N]: "))
    if resposta == 'S':
        print("Recuperando senha!")
        codigoRecuperaSenha = randint(100000, 999999)
        print(codigoRecuperaSenha)
        enviarEmail(codigoRecuperaSenha)
        codigoRecuperacaoEnviado = int(
            input("Digite o código enviado para seu Email: "))
        if codigoRecuperacaoEnviado == codigoRecuperaSenha:
            print("Senha recuperada com sucesso!")
        else:
            codigoRecuperacaoEnviado = int(
                input("Digite o código enviado para seu Email: "))
    else:
        menu()


def enviarEmail(codigo):
    mensagem = str(codigo)
    msg = email.message.Message()
    msg['Subject'] = "Recuperação Conta"
    msg['From'] = 'eduardo811laurentino@gmail.com'
    msg['To'] = 'eduardo811laurentino@gmail.com'
    password = 'akoccopkujelyjqo'
    msg.set_payload(mensagem)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print("Email enviado!")


menu()
