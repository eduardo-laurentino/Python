def programa1():
    #Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas
    primeira = input("Digite a primeira string: ")
    segunda = input("Digite a segunda string: ")
    terceira = ""
    # Para cada letra na primeira string
    for letra in primeira:
    # Se a letra está na segunda string (comum a ambas)
    # Para evitar repetidas, não deve estar na terceira.
        if letra in segunda and letra not in terceira:
            terceira += letra
    if terceira == "":
        print("Caracteres comuns não encontrados.")
    else:
        print(f"Caracteres em comum: {terceira}")


def programa2():
#Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas
    primeira = input("Digite a primeira string: ")
    segunda = input("Digite a segunda string: ")
    terceira = ""
    # Para cada letra na primeira string
    for letra in primeira:
    # Verifica se a letra não aparece dentro da segunda string
    # e também se já não está listada na terceira
        if letra not in segunda and letra not in terceira:
            terceira += letra
    # Para cada letra na segunda string
    for letra in segunda:
    # Além de não estar na primeira string,
    # verifica se já não está na terceira (evitar repetições)
        if letra not in primeira and letra not in terceira:
            terceira += letra
    if terceira == "":
        print("Caracteres incomuns não encontrados.")
    else:
        print(f"Caracteres incomuns: {terceira}")

#programa1()
programa2()