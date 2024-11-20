
class Carro:
    def __init__(self, marca, combustivel):
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, quantidade):
        self.combustivel += quantidade
        print("Abastecendo... Novo nível de combustível: " + str(self.combustivel))

    def verificar_combustivel(self):
        print("Nível de combustível: " + str(self.combustivel))