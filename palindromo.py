"""
import time
for i in range(0, 10):
    print(i, '', end=' ')
    time.sleep(0.5)
print("\n")

"""

nome = 'ana'
for i in nome:
    resp = nome[::-1]
print(resp)

if nome == resp:
    print("É palíndromo")

# validação
numero = (input('Informe seu sexo: [1/0]\n')).strip()
while numero not in '10' or numero =='':
    numero = (input('Dados Inválidos. Por Favor Informe seu Sexo: [1/0]\n')).strip()
print('Número {} registrado com sucesso'.format(numero))

