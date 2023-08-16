alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']

tBash = ['Z', 'Y', 'W', 'X', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

senha_pre_criptografada = ""
senha = input(str("Digite a sequência que deseja Criptografar: ")).upper()
for i in senha:
    if i in alfabeto:
        aux = alfabeto.index(i)
        senha_pre_criptografada = senha_pre_criptografada+""+tBash[aux]
print(senha_pre_criptografada)

senha_criptografada = ""
regra = 5
for i in senha_pre_criptografada:
    if i in alfabeto:
        aux = alfabeto.index(i)
        senha_criptografada = senha_criptografada+""+alfabeto[aux - regra]
print(senha_criptografada)

senha_descriptografada = ""
for i in senha_criptografada:
    if i in alfabeto:
        aux = alfabeto.index(i)
        senha_descriptografada = senha_descriptografada+""+alfabeto[aux + regra]
print(senha_descriptografada)

senha_inicial = ""
for i in senha_descriptografada:
    if i in tBash:
        aux = tBash.index(i)
        senha_inicial = senha_inicial+""+alfabeto[aux]
print(senha_inicial)