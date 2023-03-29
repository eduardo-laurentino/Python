class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        self.__tarifaTransferencia = 8.0
        self.__limite = 1000.00

    #NOVO MÉTODO AQUI
    def temSaldoDisponivelPara(self, valor):
        return valor < self.__saldo or self.__limite


    def saca(self, valor):

        if self.temSaldoDisponivelPara(valor):
            self.__saldo -= valor
            print(self.__saldo)
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")


    def transfere(self, valor, destino):
        valorTotal = valor + self.__tarifaTransferencia
        if self.temSaldoDisponivelPara(valorTotal):
            self.__saldo -= valorTotal
            print("Transferência efetuada.")
            print(self.__saldo)
        else:
            print("Saldo insuficiente.")


minha_conta = Conta(
    numero = int(input("Numero: ")),
    saldo = float(input("Saldo: ")),
)
#minha_conta.saca(valor = float(input("Valor Saque: ")))


conta_cliente = Conta(
    numero = int(input("Numero: ")),
    saldo = float(input("Saldo: ")),
)

minha_conta.transfere(valor = float(input("Valor: ")),
destino = int(input("Conta: "))
)
verSaldo = conta_cliente.saldo
print(verSaldo)
