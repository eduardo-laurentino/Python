import unittest
from classe_test import PesquisaAnonima

class TestPesquisaAnonima(unittest.TestCase):
    #Testes para a classe pesquisa anonima.
    def resposta_teste(self):
        #testa se uma única resposta é armazenada de forma apropriada.
        pergunta = "Que idioma você aprendeu a falar primeiro?"
        minha_pesquisa = PesquisaAnonima(pergunta)
        minha_pesquisa.guardar_resposta('Inglês')
        self.assertIn('Inglês', minha_pesquisa.guardar_resposta)
unittest.main()



#Define uma pergunta e cria uma pesquisa.

pergunta = "Que idioma você aprendeu a falar primeiro?"

minha_pesquisa = PesquisaAnonima(pergunta)

#Mostra a pergunta e armazena as respostas à pergunta.
minha_pesquisa.mostrar_pergunta()
print("Digite 'q' a qualquer momento para saair!\n")
while True:
    resposta = input("Lingua: ")
    if resposta == 'q':
        break
    minha_pesquisa.guardar_resposta(resposta)

#Exibe os resultados da pesquisa
print("Obrigado a todos que participaram da enquete!")
minha_pesquisa.mostrar_resultados()
