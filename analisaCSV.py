import csv
from matplotlib import pyplot as plt

filename = 'base_de_dados.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)
    #for index, columm_header in enumerate(header_row):
        #print(index, columm_header)

    temperaturas_maximas, temperaturas_minimas, datas = [], [], []
    for row in reader:
        temperatura_maxima = int(row[2])
        temperaturas_maximas.append(temperatura_maxima)
        temperatura_minima = int(row[3])
        temperaturas_minimas.append(temperatura_minima)
        data = row[4]
        datas.append(data)

    # Faz a plotagem dos dados
    fig = plt.figure(dpi = 100, figsize = (10, 6))
    plt.plot(datas, temperaturas_maximas, c = 'red', alpha = 0.5)
    plt.plot(datas, temperaturas_minimas, c = 'blue', alpha = 0.5)
    plt.fill_between(datas, temperaturas_maximas, temperaturas_minimas, facecolor = 'blue', alpha = 0.1)

    # Formata o gráfico
    plt.title("Temperaturas")
    plt.xlabel('', fontsize = 8)
    fig.autofmt_xdate()
    plt.ylabel("Máximas e Mínimmas", fontsize = 8)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 8)
    plt.show()