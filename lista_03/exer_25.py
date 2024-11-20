
class Pessoa:
    def __init__(self, altura, peso):
        self.altura = altura
        self.peso = peso

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)  

pessoa = Pessoa(1.75, 70)  

imc = pessoa.calcular_imc()
print(f"O IMC da pessoa é: {imc}")
