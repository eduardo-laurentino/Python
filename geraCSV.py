import csv
import random
from datetime import datetime

# Defina o nome do arquivo CSV e o número de linhas desejado
nome_arquivo = "base_de_dados.csv"
num_linhas = 31  # Altere para o número desejado de linhas

# Crie dados fictícios
dados = []
for i in range(1, num_linhas + 1):
    #cidade = random.choice(["Passagem Franca", "Lagoa do Mato", "Buriti Bravo", "Caxias", "Aldeias Altas"])
    cidade = "Caxias"
    temperatura_maxima = random.randint(25, 29)
    temperatura_minima = random.randint(20, 24)
    dia = i
    mes = 'Janeiro'
    #mes = random.choice(["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"])
    ano = 2023
    data = str(dia) + "-" + mes + "-" + str(ano)

    linha = [i, cidade, temperatura_maxima, temperatura_minima, data]
    dados.append(linha)

# Escreva os dados no arquivo CSV
with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    # Escreva o cabeçalho
    escritor_csv.writerow(["ID", "Cidade", "Temperatura Máxima", "Temperatura Mínima", "Data"])
    # Escreva os dados
    for linha in dados:
        escritor_csv.writerow(linha)

print(f"Base de dados CSV '{nome_arquivo}' criada com {num_linhas} linhas.")