#Verifique se a segunda ocorre dentro da primeira e imprima a posição de início
primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
posição = primeira.find(segunda)
#O método "find" retorna a posição de inicio da substring na string.
if posição == -1:
    print(f"'{segunda}' não encontrada em '{primeira}'")
else:
    print(f"{segunda} encontrada! Inicia na posição {posição} de {primeira}")