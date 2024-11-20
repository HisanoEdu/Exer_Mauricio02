
class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(self.som)

if __name__ == "__main__":
    animal = Animal("Cachorro", "Au au")
    
    animal.emitir_som()

gato=Animal("Gato","Miau Miau")

gato.emitir_som()