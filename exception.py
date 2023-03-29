#Se o bloco try funcionar, Python ignorará o bloco except. Se o código do bloco try causar um erro o código procurará o bloco except e lançará a exceção
try:
    print(5/0)
except ZeroDivisionError:
    print("Não existe divisão por zero!")

print("Digite dois números, e eu vou dividí-los!")
print("Digite 'q' para sair!")

while True:
    primeiro_numero = input("Pimeiro número: ")
    if primeiro_numero == 'q':
        break
    segundo_numero = input("Segundo Número: ")
    if segundo_numero == 'q':
        break
    try:
        resposta = int(primeiro_numero) / int(segundo_numero)
    except:
        print("Não existe divisão por zero!")
    else:
        print(resposta)


filename = 'Alice.txt'
def conta_palavras(filename):
    try:
        with open(filename) as file_object:
            conteudo = file_object.read()
    except FileNotFoundError:
        #Para python não informar uma mensagem de erro use a palavra Pass. É a chamada falha silenciosa.
        #print("Desculpe, o arquivo " + filename + " não existe!")
        pass
    else:
        palavras = conteudo.split()
        numero_palavras = len(palavras)
        print("O arquivo " + filename + " tem " + str(numero_palavras) + " palavras")

arquivo = ['write.txt', 'alice.txt', 'Alice.txt', 'arquivo.txt']

#for i in arquivo:
    #conta_palavras(i)
    
while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    if num1 == 'q' or num2 == 'q':
        break
    else:
        try:
            soma = int(num1) + int(num2)
        except ValueError:
            print("Digite apenas números!")
        else:
            print(soma)
