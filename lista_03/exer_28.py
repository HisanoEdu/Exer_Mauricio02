
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        self.contas.append(conta)

    def listar_saldos(self):
        
        for conta in self.contas:
            print("Titular: " + conta.titular + " | Saldo: R$" + str(conta.saldo))

banco = Banco()

banco.adicionar_conta("João", 1000)
banco.adicionar_conta("Maria", 500)
banco.adicionar_conta("Pedro", 1200)

banco.listar_saldos()

