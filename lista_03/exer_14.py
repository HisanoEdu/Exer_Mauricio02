
class Eletrodomestico:
    def __init__(self, nome, potencia):
        
        self.nome = nome
        self.potencia = potencia

    def ligar(self):
    
        print("O " + self.nome + " de " + str(self.potencia) + "W foi ligado.")


eletro = Eletrodomestico("Liquidificador", 500)


eletro.ligar()
