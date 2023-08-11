expressao = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(expressao):
    if expressao[x] == "(":
        pilha.append("(")
    if expressao[x] == ")":
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            pilha.append(")") # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")