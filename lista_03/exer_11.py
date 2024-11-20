
class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$" + str(valor) + " realizado com sucesso.")
    
    def sacar(self, valor):
        
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque de R$" + str(valor) + " realizado com sucesso.")
        else:
            print("Saldo insuficiente para saque de R$" + str(valor))

    def exibir_saldo(self):
        
        print("Saldo atual: R$" + str(self.saldo))


conta = ContaBancaria()

conta.depositar(1000)   
conta.sacar(500)        
conta.exibir_saldo()    
conta.sacar(600)        
conta.exibir_saldo()
