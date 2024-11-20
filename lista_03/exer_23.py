
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, percentual):
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print("Aumento de R$" + str(aumento) + " aplicado.")
        print("Novo salário de " + self.nome + ": R$" + str(self.salario))

funcionario = Funcionario("Carlos", 3000)
funcionario.calcular_aumento(10)
