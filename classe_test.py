class PesquisaAnonima():
    #Coleta respostas anônimas para uma pergunta de uma pesquisa.
    def __init__(self, pergunta):
        #Armazena uma pergunta e se prepara para armazenar as respostas.
        self.pergunta = pergunta
        self.resposta = []
    def mostrar_pergunta(self):
        #Mostra a pergunta da pesquisa.
        print(self.pergunta)
    def guardar_resposta(self, nova_resposta):
        #Armazena uma única resposta da pesquisa.
        self.resposta.append(nova_resposta)
    def mostrar_resultados(self):
        #Mostra todas as respostas dadas.
        print("RESULTADOS DA PESQUISA: ")
        for res in self.resposta:
            print("- " + res)
            