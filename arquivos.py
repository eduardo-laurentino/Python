
arq = 'arquivo.txt'
#Analisando arquivo original
with open(arq) as file_object:
        #Readlines armazena em uma lista
        lines = file_object.readlines()
#print(lines)

#Analisado o arquivo linha por linha
for line in lines:
        #print(line.rstrip())
        print("\n")

#Removendo espaços em branco 
arq_string = ''
for line in lines:
        arq_string += line.strip()
print(arq_string)
print(len(arq_string))

birthday = input("Digite a sua data de nascimento: ")
if birthday in arq_string:
        print("A data do seu nascimento está no arquivo\n")
else:
        print("A data do seu nascimento não está no arquivo\n")


var = str(arq_string.replace('33', '00'))
print(var)

arqv = 'write.txt'
with open(arqv, 'a') as file_object:
        #Para exibir várias linhas devemos usar o caractere de quebra de linha
        #Cada vez que rodar o código o que já foi escrito não será mais escrito no arquivo
        #Não substitui palavras já escrita com a função Write
        #Não reescreve a mesma função Write
        aux = True
        while aux:
                nome = str(input("Digite seu nome, [x] para sair ou [e] para exibir nomes : "))
                if nome == 'x':
                        aux = False
                elif nome == 'e':
                        with open(arqv, 'r') as leitura:
                                arquivo_leitura = leitura.readlines()
                                for i in arquivo_leitura:
                                        print("Olá", i.strip())
                else:
                        file_object.writelines(nome + '\n')
