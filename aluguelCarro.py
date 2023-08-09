km = int(input("Digite a quantidade de quilometros percorridos:"))
dias = int(input("Digite quantos dias você ficou com o carro:"))
preco_por_dia = 60
preco_por_km = 0.15
preco_a_pagar = km * preco_por_km + dias * preco_por_dia
print("Total a pagar: R$ {:.2f} ".format(preco_a_pagar))