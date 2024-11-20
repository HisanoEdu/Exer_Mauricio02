
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outra_pessoa):
        print("Olá, " + outra_pessoa.nome + "!")

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("Maria")

pessoa1.cumprimentar(pessoa2)
