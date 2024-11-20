
class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

calc = Calculadora()
resultado_soma = calc.somar(10, 5)
print("Resultado da soma: ", resultado_soma)

resultado_subtracao = calc.subtrair(10, 5)
print("Resultado da subtração: ", resultado_subtracao)
