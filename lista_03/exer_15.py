
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        area = self.lado ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 4 * self.lado
        return perimetro

quadrado = Quadrado(5)

area = quadrado.calcular_area()
perimetro = quadrado.calcular_perimetro()

print("Área do quadrado: " + str(area))
print("Perímetro do quadrado: " + str(perimetro))
