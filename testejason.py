import json 
#Testes Simples
#numeros = [2, 3, 5, 7, 11, 13]
filename = 'numeros.jason'
#with open(filename, 'w') as file_object:
    #json.dump(numeros, file_object)
    
"""
with open(filename) as file_object:
    numeros = json.load(file_object)
print(numeros)


nome_usuario = input("Qual o seu nome?")
with open(filename, 'w') as file_object:
    json.dump(nome_usuario, file_object)
    print("Nós vamos lembrar de você quando você voltar, " + nome_usuario + "!")
    
"""
def nome_usuario_armazenado():
    #Se o arquivo existir o try será executado
    try:
        with open(filename) as file_object:
            nome_usuario = json.load(file_object)
    except FileNotFoundError:
        #Se o arquivo não existir o except será executado. Um nome será informado e a próxima execução cai no else e o nome será lembrado.
        return None
    else:
        return nome_usuario



def cumprimentar_usuario():
    nome_usuario = nome_usuario_armazenado()
    if nome_usuario:
        print("Bem vindo de volta, " + nome_usuario + "!")
    else:
        nome_usuario = input("Qual o seu nome?")
        with open(filename, 'w') as file_object:
            json.dump(nome_usuario, file_object)
            print("Nós vamos lembrar de você quando você voltar, " + nome_usuario + "!")

cumprimentar_usuario()