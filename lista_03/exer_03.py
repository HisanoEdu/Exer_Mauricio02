
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        print('Marca:' + self.marca)
        print('Ano:'+ self.ano)

if __name__ == "__main__":
    carro = Carro("Ford", 2020)

    carro.exibir_informacoes()
