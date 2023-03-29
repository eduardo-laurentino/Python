import unittest
from nomeFormatado import nome_formatado

class testeNome(unittest.TestCase):
    def teste_nome_sobrenome(self):
        nome_completo = nome_formatado('janis', 'joplin')
        self.assertEqual(nome_completo, 'Janis joplin')
unittest.main()

print("Digite 'q' a qualquer momento para sair!")
while True:
    nome = input("Digite seu nome: ")
    if nome == 'q':
        break
    sobrenome = input("Digite seu sobrenome: ")
    if sobrenome == 'q':
        break
    else:
        nome_completo = nome_formatado(nome, sobrenome)
        print("O seu nome completo é: " + nome_completo + ".")
