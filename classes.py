# Criando a classe Carro
"""class Carro():
    def __init__(self, modelo, cor, categoria, ano, marca):
        # Criando os atributos
        self.modelo = modelo.title()
        self.cor = cor.title()
        self.categoria = categoria.title()
        self.ano = ano
        self.marca = marca.title()
# Criando os métodos
    def viajando(self, pedal):
        # Verificando ações do objeto
        funcionalidades = ['acelerar', 'parar', 'buzinar']
        if pedal in funcionalidades:
            print(pedal, "o carro!")
        else:
            return ("Instrução inválida para este veículo")

# Criando o objeto novo_carro
novo_carro = Carro('hilux', 'vermelho', 'camionete', '2020', 'toyota')
print(novo_carro.modelo)

novo_carro.viajando('parar')"""


class Restaurantes:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def restaurante_aberto(self):
        mensagem = "Aberto Agora. Sejam Bem-Vindos!"
        return mensagem


novo_restaurante = Restaurantes('Comida Caseira')
print(novo_restaurante.restaurante_aberto())
