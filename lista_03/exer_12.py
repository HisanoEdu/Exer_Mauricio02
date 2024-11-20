
class Filme:
    def __init__(self, titulo, duracao):
    
        self.titulo = titulo
        self.duracao = duracao

    def exibir_detalhes(self):

        print("Título: " + self.titulo)
        print("Duração: " + str(self.duracao) + " horas" )

filme = Filme("Vingadores Ultimato",3)

filme.exibir_detalhes()
