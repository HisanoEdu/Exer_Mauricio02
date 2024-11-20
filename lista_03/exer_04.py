class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_detalhes(self):
        print('Título: ' + self.titulo)
        print('Autor: ' + self.autor)

if __name__ == "__main__":
    livro = Livro("Duna","Frank Herbert")
    
    livro.exibir_detalhes()

oda=livro("One Piece","Eiichiro Oda")

oda.exibir_detalhes()