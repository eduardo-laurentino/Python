alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']

atBash = ['Z', 'Y', 'W', 'X', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

senha_pre_criptografada = ""
senha = str(input("Digite a sequência que deseja Criptografar: ")).upper()
regra = int(input("Digite a regra de Criptografia: "))
if regra > 0:
    print("Regra de Criptografia inválida!")
else:
    regra = abs(regra)
    for i in senha:
        if i in alfabeto:
            senha_pre_criptografada = senha_pre_criptografada+""+atBash[alfabeto.index(i)]
    print(senha_pre_criptografada)

    senha_criptografada = ""
    for i in senha_pre_criptografada:
        if i in alfabeto:
            aux = regra - alfabeto.index(i)
            while aux >= len(alfabeto):
                aux -= len(alfabeto)
            senha_criptografada = senha_criptografada+""+alfabeto[aux-1]
    print(senha_criptografada)

    senha_descriptografada = ""
    for i in senha_criptografada:
        if i in alfabeto:
            auxDes = regra - alfabeto.index(i)
            while auxDes >= len(alfabeto):
                auxDes -= len(alfabeto)
            senha_descriptografada = senha_descriptografada+""+alfabeto[auxDes-1]
    print(senha_descriptografada)

    senha_inicial = ""
    for i in senha_descriptografada:
        if i in atBash:
            senha_inicial = senha_inicial+""+alfabeto[atBash.index(i)]
    print(senha_inicial)