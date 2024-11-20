
class ConversorMoeda:
    def __init__(self, taxa_conversao):
        self.taxa_conversao = taxa_conversao

    def converter_para_reais(self, dolares):
        reais = dolares * self.taxa_conversao
        return reais

conversor = ConversorMoeda(6.2)  

valor_em_reais = conversor.converter_para_reais(100)

print("100 dólares equivalem a R$" + str(valor_em_reais))
