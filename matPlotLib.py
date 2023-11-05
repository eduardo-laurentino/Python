import matplotlib.pyplot as plt
from random import randint
import pygal

"""
def  testeMatPlotLib():
    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]
    #x_values = [1, 2, 3, 4, 5]
    #y_values = [1, 4, 9, 16, 25]
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    # Plota o gráfico e controla a espessura da linha
    #plt.plot(input_values ,squares, linewidth = 5)
    # Define um titulo para o gráfico
    plt.title("Square Numbers", fontsize = 24)
    # Define um rótulo para o eixo X
    plt.xlabel("Value", fontsize = 14)
    # Define um rótulo para o eixo Y
    plt.ylabel("Square of value", fontsize = 14)

    # Estiliza as marcações nos eixoa x e y
    plt.tick_params(axis='both', labelsize = 14)

    #plt.scatter(x_values, y_values, c='red', s = 40)
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s = 40)

    # Salva o gráfico
    plt.savefig("Squares_plot.png")
    # Exibe o gráfico
    plt.show()
"""

class Dado():
    def __init__(self, num_lados = 6):
        self.num_lados = num_lados

    def lancar_dado(self):
        return randint(1, self.num_lados)
    
dado1 = Dado()
dado2 = Dado()
resultados_lancamentos = []
for num_lancamentos in range(500):
    resultado_lancamento = dado1.lancar_dado() + dado2.lancar_dado()
    resultados_lancamentos.append(resultado_lancamento)
print(resultados_lancamentos)

# Analisando os resultados
frequencia = []
resultado_maximo = dado1.num_lados + dado2.num_lados
for value in range(2, resultado_maximo + 1):
    frequency = resultados_lancamentos.count(value)
    frequencia.append(frequency)
print(frequencia)

histograma = pygal.Bar()

histograma.title = "Resultados de lançar dois dados 500 vezes!"
#histograma.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
histograma.x_labels = list(range(2, resultado_maximo+1))
histograma.x_title = "Resultado"
histograma.y_title = "Frequência dos Resultados!"

histograma.add('Dado', frequencia)
histograma.render_to_file('dado_visual.svg')
