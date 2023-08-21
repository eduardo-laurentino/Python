from random import randint

senha = input("Digite a senha que você quer encontrar: ")
combinacoes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '*', '(', ')', '{', '}', '[', ']', '^', '~', '?', '/', '&']

achou = ""
while (achou != senha):
    achou = ""
    for caractere in senha:
        achouCaractere = combinacoes[randint(0, 52)]
        achou = str(achouCaractere)+str(achou)
    print(achou)