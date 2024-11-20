
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
    
        return self.largura * self.altura

retangulo1 = Retangulo(5, 10)

area = retangulo1.calcular_area()
print(f"A área do retângulo é: {area} unidades quadradas")

