cigarros_por_dia = int(input("Quantidade de cigarros por dia:"))
anos_fumando = float(input("Quantidade de anos fumando:"))
reducao_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
reducao_em_dias = reducao_em_minutos // (24 * 60)
print(f"Redução do tempo de vida = {reducao_em_dias} dias.")