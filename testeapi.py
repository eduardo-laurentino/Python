import requests
import pygal


link = 'https://monitoramentopiscicultura.eduardolaurenti.repl.co/dados'
#link = 'https://apiautomacao.eduardolaurenti.repl.co/dadosLeds'


def busca_dados_API():
    requisicao = requests.get(link)
    if requisicao.status_code == 200:
        return (requisicao.json())
    else:
        return (f'Erro na solicitação GET. Código de status: {requisicao.status_code}')


def envia_dados_API():
    dados = {"led1": "OFF", "led6": "ON"}

    # Fazer a solicitação POST
    response = requests.put(link, json=dados)

    # Verificar a resposta da API
    if response.status_code == 200:
        print('Dados adicionados com sucesso!')
    else:
        print('Erro ao adicionar dados à API. Código de status:',
              response.status_code)


dados = busca_dados_API()
horas, temperaturas, ph, turbidity = [], [], [], []
for dado in dados:
    hora = dado['hora']
    horas.append(hora)
    temperatura = dado['temperatura']
    temperaturas.append(float(temperatura))
    pH = dado['ph']
    ph.append(float(pH))
    turbidez = dado['turbidez']
    turbidity.append(float(turbidez))

grafico = pygal.Bar()
grafico.title = "Análise piscicultura"

grafico.x_labels = horas
grafico.x_title = "Hora"
grafico.y_title = "Temperaturas, Turbidez, pH"

grafico.add('Temperatura', temperaturas)
grafico.add('pH', ph)
grafico.add('Turbidez', turbidity)
grafico.render_to_file('dados_piscicultura.svg')
