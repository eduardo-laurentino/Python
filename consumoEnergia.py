consumo = int(input("Consumo em kWh: "))
tipo = input("Tipo da instalação (R, C ou I): ")
#Residencial
if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
#Industrial
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
#comercial
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
custo = consumo * preco
print(f"Valor a pagar: R$ {custo:.2f}")