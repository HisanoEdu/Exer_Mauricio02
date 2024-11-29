
class Veiculo:
    def __init__(self, marca, modelo):  
        self.marca = marca
        self.modelo = modelo

    def tipo_combustivel(self):
        return "Desconhecido"

    def capacidade_passageiros(self):
        return 0

class Carro(Veiculo):
    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 5

class Moto(Veiculo):
    def tipo_combustivel(self):
        return "Gasolina"

    def capacidade_passageiros(self):
        return 2

class Caminhao(Veiculo):
    def tipo_combustivel(self):
        return "Diesel"

    def capacidade_passageiros(self):
        return 2

def demonstrar_veiculos():
    veiculos = [
        Carro("Toyota", "Corolla"),
        Moto("Honda", "CB500"),
        Caminhao("Volvo", "FH540")
    ]

    for veiculo in veiculos:
        print("Marca: " + veiculo.marca)
        print("Modelo: " + veiculo.modelo)
        print("Tipo de Combustível: " + veiculo.tipo_combustivel())
        print("Capacidade de Passageiros: " + str(veiculo.capacidade_passageiros()))
        
demonstrar_veiculos()

