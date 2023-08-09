class Cliente:
    def __init__(self, cpf, nome, sobrenome):
        self.cpf = cpf
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.contatos = []

    def salvar_contatos(self, numero):
        self.contato = Contatos(numero)
        self.contatos.append(self.contato)

    def abrir_conta_poupança(self, numero_conta, agencia, saldo):
        self.cp = Poupanca(numero_conta, agencia, saldo)

    def abrir_conta_corrente(self, numero_conta, agencia, saldo):
        self.cc = Corrente(numero_conta, agencia, saldo)


class Conta:
    def __init__(self, numero_conta, agencia, saldo):
        self.numero = numero_conta
        self.agencia = agencia
        self.saldo = float(saldo)

    def ver_saldo(self):
        return self.saldo

    def cadastrar_chave_pix(self, chave_pix):
        self.chave_pix = Pix(chave_pix)

    def depositar(self, valor):
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        if self.saldo < valor or valor < 0:
            print("SALDO INSUFICIENTE!!")
        else:
            self.saldo -= valor
            self.saldo -= valor*self.taxa_transferencia
            conta_destino.depositar(valor)
            print("TRANSFERÊNCIA REALIZADA COM SUCESSO!!")

    def saque (self, valor):
        if self.saldo < valor or valor < 0:
            print("SALDO INSUFICIENTE!!")
        else:
            self.saldo -= valor
            print("SAQUE REALIZADO COM SUCESSO!!")



class Pix:
    def __init__(self, chave_pix):
        self.pix = chave_pix

    def ver_chave_pix(self):
        return self.pix


class Contatos:
    def __init__(self, numero):
        self.numero = numero

    def ver_contatos(self):
        return self.numero


class Corrente(Conta):
    def __init__(self, numero_conta, agencia, saldo):
        super().__init__(numero_conta, agencia, saldo)
        self.taxa_transferencia = 0.05


class Poupanca(Conta):
    def __init__(self, numero_conta, agencia, saldo):
        super().__init__(numero_conta, agencia, saldo)
        self.taxa_transferencia = 0.025


# Criando conta CORRENTE para cliente 1
cliente1 = Cliente('347378', 'eduardo', 'laurentino')
cliente1.abrir_conta_corrente('11231', '2412', '3000.00')
cliente1.cc.cadastrar_chave_pix('1234')
cliente1.salvar_contatos('984999995')

print("===== DADOS CLIENTE 1 =====")
print("CONTA CORRENTE")
print("NOME: ", cliente1.nome, cliente1.sobrenome)
print("SALDO: ", cliente1.cc.ver_saldo())
print("CHAVE-PIX: ", cliente1.cc.chave_pix.ver_chave_pix())
print("TELEFONE: ", cliente1.contato.ver_contatos())
print("\n")

# Criando conta POUPANÇA para cliente 1
cliente1 = Cliente('347378', 'eduardo', 'laurentino')
cliente1.abrir_conta_poupança('11231', '2412', '500.00')
cliente1.cp.cadastrar_chave_pix('1234')
cliente1.salvar_contatos('984999995')

print("===== DADOS CLIENTE 1 =====")
print("CONTA POUPANÇA")
print("NOME: ", cliente1.nome, cliente1.sobrenome)
print("SALDO: ", cliente1.cp.ver_saldo())
print("CHAVE-PIX: ", cliente1.cp.chave_pix.ver_chave_pix())
print("TELEFONE: ", cliente1.contato.ver_contatos())
print("\n")

# Criando conta CORRENTE para cliente 2
cliente2 = Cliente('3423478', 'maria', 'sousa')
cliente2.abrir_conta_corrente('09231', '1012', '6000.00')
cliente2.cc.cadastrar_chave_pix('9834')
cliente2.salvar_contatos('984003895')

print("===== DADOS CLIENTE 2 =====")
print("CONTA CORRENTE")
print("NOME: ", cliente2.nome, cliente2.sobrenome)
print("SALDO: ", cliente2.cc.ver_saldo())
print("CHAVE-PIX: ", cliente2.cc.chave_pix.ver_chave_pix())
print("TELEFONE: ", cliente2.contato.ver_contatos())

# Criando conta POUPANÇA para cliente 2
cliente2 = Cliente('3423478', 'maria', 'sousa')
cliente2.abrir_conta_poupança('09231', '1012', '10000.00')
cliente2.cp.cadastrar_chave_pix('9834')
cliente2.salvar_contatos('984003895')
print("\n")

print("===== DADOS CLIENTE 2 =====")
print("CONTA POUPANÇA")
print("NOME: ", cliente2.nome, cliente2.sobrenome)
print("SALDO: ", cliente2.cp.ver_saldo())
print("CHAVE-PIX: ", cliente2.cp.chave_pix.ver_chave_pix())
print("TELEFONE: ", cliente2.contato.ver_contatos())
print("\n")


cliente1.cp.transferir(300, cliente2.cp)
print(cliente2.cp.ver_saldo())
print(cliente1.cp.ver_saldo())

cliente1.cp.saque(300)
print(cliente1.cp.ver_saldo())