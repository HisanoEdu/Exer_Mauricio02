
class Pessoa:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def verificar_altura(self):
        if self.altura > 1.75:
            print(self.nome + " é mais alta que 1,75 m.")
        else:
            print(self.nome + " não é mais alta que 1,75 m.")

pessoa = Pessoa("Sebek", 1.88)
pessoa.verificar_altura()


nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura em metros (ex: 1.80): "))

pessoa = Pessoa(nome, altura)
pessoa.verificar_altura()
