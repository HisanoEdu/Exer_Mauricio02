
class Produto:
    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco *= (1 - porcentagem / 100)

if __name__ == "__main__":

    produto = Produto("Camiseta", 50.00)
    
    print('Preço original de {produto.nome}: R${produto.preco:.2f}')
    
    produto.aplicar_desconto(10)
    
    print('Preço com desconto de 10%: R${produto.preco:.2f}')
