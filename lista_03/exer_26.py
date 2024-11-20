
class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(str(a) + " + " + str(b) + " = " + str(resultado))
        return resultado

    def subtrair(self, a, b):
        resultado = a - b
        self.historico.append(str(a) + " - " + str(b) + " = " + str(resultado))
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historico.append(str(a) + " * " + str(b) + " = " + str(resultado))
        return resultado

    def dividir(self, a, b):
        if b != 0:
            resultado = a / b
            self.historico.append(str(a) + " / " + str(b) + " = " + str(resultado))
            return resultado
        else:
            self.historico.append(str(a) + " / " + str(b) + " = Erro (divisão por zero)")
            return "Erro (divisão por zero)"

    def exibir_historico(self):
        if len(self.historico) == 0:
            print("Nenhuma operação realizada.")
        else:
            for operacao in self.historico:
                print(operacao)

calc = Calculadora()
print(calc.somar(5, 3))
print(calc.subtrair(10, 4))
calc.exibir_historico()

