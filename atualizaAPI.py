"""
dados = {'dia_semana':'Terca','data':'05/10/2023','hora':'07:20:00','temperatura':30.8,'turbidez':50.5,'ph':7.0}

print(dados)

def atualizaAPI(chave, valor):
    for chaveApi in dados.keys():
        if chaveApi == chave:
            print("Chave API = ",chaveApi)
            print("Chave fornecida = ", chave)
            dados[chaveApi] = valor
            break

atualizaAPI('turbide', 40.5)
print(dados)

"""

import requests

# URL da API que você deseja atualizar
url = 'https://apiautomacao.eduardolaurenti.repl.co/dadosLeds/123'  # Substitua pelo URL da sua API

# Dados que você deseja atualizar (chave e valor)
dados_atualizados = {
    'led2': 'ON',
    # Adicione mais chaves e valores conforme necessário
}

# Envie a solicitação PUT com os dados atualizados no corpo da solicitação
response = requests.put(url, json=dados_atualizados)

# Verifique a resposta da API
if response.status_code == 200:
    print('Dados atualizados com sucesso!')
elif response.status_code == 404:
    print('Recurso não encontrado na API.')
else:
    print(f'Erro na atualização. Código de status: {response.status_code}')