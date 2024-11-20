
class Veiculo:
    def __init__(self, modelo, velocidade):
        
        self.modelo = modelo
        self.velocidade = velocidade

    def aumentar_velocidade(self, aumento):

        self.velocidade += aumento
        print("Velocidade aumentada em " + str(aumento) + " km/h.")
        print("Velocidade atual: " + str(self.velocidade) + " km/h.")

veiculo = Veiculo("Fusca", 60)

print("Velocidade inicial: " + str(veiculo.velocidade) + " km/h")
veiculo.aumentar_velocidade(20)  # Aumenta a velocidade em 20 km/h
