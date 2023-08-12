def aluguelCarro():
    km = int(input("Digite a quantidade de quilometros percorridos:"))
    dias = int(input("Digite quantos dias você ficou com o carro:"))
    preco_por_dia = 60
    preco_por_km = 0.15
    preco_a_pagar = km * preco_por_km + dias * preco_por_dia
    print("Total a pagar: R$ {:.2f} ".format(preco_a_pagar))

def consumoEnergia():
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

def converterTemperatura():
    c = float(input("Digite a temperatura em °C:"))
    f = (9 * c / 5) + 32
    print(f" {c}°C é igual a {f}°F")

def contarLetras():
    frase = input("Digite uma frase para contar as letras:")
    d = {}
    for letra in frase:
        if letra in d:
            d[letra] = d[letra] + 1
        else:
            d[letra] = 1
    print(d)

def palindromo():
    nome = input("Digite uma frase e veja se é Palíndromo: ")
    for i in nome:
        resp = nome[::-1]
    print(resp)

    if nome == resp:
        print("É palíndromo")

def tempoViagem():
    distância = float(input("Digite a distância em km:"))
    velocidade_média = float(input("Digite a velocidade média em km/h:"))
    tempo = distância / velocidade_média
    print("O tempo estimado é de {:.2f} horas".format(tempo))
    # Opcional: imprimir o tempo em horas, minutos e segundos
    tempo_s = int(tempo * 3600) # convertemos de horas para segundos
    horas = int(tempo_s / 3600) # parte inteira
    tempo_s = int(tempo_s % 3600) # o resto
    minutos = int(tempo_s / 60)
    segundos = int(tempo_s % 60)
    print(f"{horas}:{minutos}:{segundos}")

def tempoVidaFumante():
    cigarros_por_dia = int(input("Quantidade de cigarros por dia:"))
    anos_fumando = float(input("Quantidade de anos fumando:"))
    reducao_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
    # Um dia tem 24 x 60 minutos
    reducao_em_dias = reducao_em_minutos // (24 * 60)
    print(f"Redução do tempo de vida = {reducao_em_dias} dias.")

def multiplicacao():
    p = int(input("Primeiro número: "))
    s = int(input("Segundo número: "))
    x = 1
    r = 0
    while x <= s:
        r = r + p
        x = x + 1
    print(f"{p} x {s} = {r}")

def menorNaLista():
    l = [4, 2, 1, 7]
    mínimo = l[0]
    for e in l:
        if e < mínimo:
            mínimo = e
    print(mínimo)

def listaDecrescente():
    lista = [1, 2, 3, 4, 5]
    fim = 5
    while fim > 1:
        trocou = False
        x = 0
        while x < (fim-1):
            if lista[x] < lista[x+1]: # Apenas a condição de verificação foi alterada
                trocou = True
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
                #print(temp)
                #print(lista[x])
                #print(lista)
                x += 1
        if not trocou:
            break
        fim -= 1
    for i in lista:
        print(i)

def emprestimo():
    valor = float(input("Digite o valor da casa: "))
    salário = float(input("Digite o salário: "))
    anos = int(input("Quantos anos para pagar: "))
    meses = anos * 12
    prestacao = valor / meses
    if prestacao > salário * 0.3:
        print("Infelizmente você não pode obter o empréstimo")
    else:
        print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")

def divisao():
    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    quociente = 0
    x = dividendo
    while x >= divisor:
        x = x - divisor
        quociente = quociente + 1
        resto = x
    print(f"{dividendo} / {divisor} = {quociente} resto {resto}")

def verificadorParenteses():
    expressao = input("Digite a sequência de parênteses a validar:")
    x = 0
    pilha = []
    while x < len(expressao):
        if expressao[x] == "(":
            pilha.append("(")
        if expressao[x] == ")":
            if len(pilha) > 0:
                pilha.pop(-1)
            else:
                pilha.append(")") # Força a mensagem de erro
                break
        x = x + 1
    if len(pilha) == 0:
        print("OK")
    else:
        print("Erro")

def deposito():
    deposito = float(input("Depósito inicial: "))
    taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
    mes = 1
    saldo = deposito
    while mes <= 24:
        saldo = saldo + (saldo * (taxa / 100))
        print(f"Saldo do mês {mes} é de R${saldo:.2f}.")
        mes = mes + 1
    print(f"O ganho obtido com os juros foi de R${saldo - deposito:.2f}")

def nomeFormatado(nome, sobrenome):
    nome_completo = nome + " " + sobrenome
    return nome_completo.title()

def temperaturaMaxMin():
    temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]
    #A escolha do primeiro elemento é arbitrária, poderia ser qualquer elemento válido
    minima = temperaturas[0] 
    maxima = temperaturas[0]
    soma = 0
    for i in temperaturas:
        if i < minima:
            minima = i
        if i > maxima:
            maxima = i
        soma = soma + i
    print(f"Temperatura máxima: {maxima} °C")
    print(f"Temperatura mínima: {minima} °C")
    print(f"Temperatura média: {soma / len(temperaturas)} °C")

def tabuada():
    n = int(input("Tabuada de:"))
    x = 1
    while x <= 10:
        print(f"{n} x {x} = {n * x}")
        x = x + 1
    print("\n\n")

    n = int(input("Tabuada de: "))
    inicio = int(input("De: "))
    fim = int(input("Até: "))
    x = inicio
    while x <= fim:
        print(f"{n} x {x} = {n * x}")
        x = x + 1

#aluguelCarro()
#consumoEnergia()
#converterTemperatura()
#contarLetras()
#palindromo()
#tempoViagem()
#tempoVidaFumante()
#multiplicacao()
#menorNaLista()
#listaDecrescente()
#emprestimo()
#divisao()
#verificadorParenteses()
#deposito()
#print(nomeFormatado("eduardo", "laurentino"))
#tabuada()
temperaturaMaxMin()