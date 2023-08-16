turismo = ['Lençóis Maranhenses', 'Pantanal', 'Serra da Capivara', 'Poço Azul', 'Mato Grosso do Sul']
print(turismo)
print('\n')
print(sorted(turismo))
print('\n')
inverso = sorted(turismo)
inverso.sort(reverse = True)
print(inverso)
print('\n')
print(turismo)
turismo.reverse()
print(turismo)
turismo.reverse()
print(turismo)
print('\n')
turismo.sort()
print(turismo)
turismo.sort(reverse = True)
print(turismo)

tamanho = len(turismo)
print(tamanho)

nomes = ['Eduardo', 'Maria']
for nome in nomes:
    print("Olá, "+nome.title())



numeros = []
for valor in range (1, 11):
    numeros.append(valor**2)
print(numeros)

num = []
num = list(range(1, 6))
print(num)


# Usando list comprehension

print('\n')
print('Usando list comprehension')

digitos = [valor**2 for valor in range(1, 11)]
print(digitos)
