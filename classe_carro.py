class Carro:
    def __init__(self, marca, modelo, categoria, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.categoria = categoria
        self.ano = ano
        self.placa = placa

    def criar_flex(self, marca, modelo, categoria, ano, placa):
        self.cf = CarroFlex(marca, modelo, categoria, ano, placa)
    
    def ver_carro(self):
        return self.marca, self.modelo, self.categoria, self.ano, self.placa, self.combustivel
    

class CarroFlex(Carro):
    def __init__(self, marca, modelo, categoria, ano, placa):
        super().__init__(marca, modelo, categoria, ano, placa)
        self.combustivel = 'Gasolina'

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, categoria, ano, placa):
        super().__init__(marca, modelo, categoria, ano, placa)
        self.combustivel = 'Elétrico'

class CarroDiesel(Carro):
    def __init__(self, marca, modelo, categoria, ano, placa):
        super().__init__(marca, modelo, categoria, ano, placa)
        self.combustivel = 'Diesel'

c1 = Carro
c1.criar_flex('fiat', 'strada', 'Picape', '2020', 'nxa2432')
print(c1.ver_carro())
