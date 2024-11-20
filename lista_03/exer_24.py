
class Elevador:
    def __init__(self, totalAndares):
        self.andarAtual = 0  
        self.totalAndares = totalAndares

    def subir(self):

        if self.andarAtual < self.totalAndares:
            self.andarAtual += 1
            print(f"Subindo para o andar {self.andarAtual}.")
        else:
            print("Você já está no último andar.")

    def descer(self):
        
        if self.andarAtual > 0:
            self.andarAtual -= 1
            print(f"Descendo para o andar {self.andarAtual}.")
        else:
            print("Você já está no térreo.")

elevador = Elevador(10)

elevador.subir() 
elevador.subir()  
elevador.descer() 
elevador.descer()
elevador.descer() 
