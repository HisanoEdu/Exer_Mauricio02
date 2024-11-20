
class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.estoque = estoque

    def exibir_detalhes(self):

        print("Título: " + self.titulo)
        print("Autor: " + self.autor)
        print("Quantidade em estoque: " + str(self.estoque))

    def vender_livro(self):
        if self.estoque > 0:
            self.estoque -= 1
            print("Livro vendido! Estoque atual: " + str(self.estoque))
        else:
            print("Não há mais livros em estoque.")

livro = Livro("O Alquimista", "Paulo Coelho", 10)
livro.exibir_detalhes()

livro.vender_livro()

