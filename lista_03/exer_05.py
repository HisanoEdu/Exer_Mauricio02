
import math

class Circulo:
    def __init__(self, raio):
    
        self.raio = raio

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

if __name__ == "__main__":
    circulo = Circulo(5)
    
    perimetro = circulo.calcular_perimetro()
    print('Perímetro do círculo:', perimetro)
