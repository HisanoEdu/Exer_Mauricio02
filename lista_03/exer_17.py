
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatar_data(self):
        return str(self.dia).zfill(2) + "/" + str(self.mes).zfill(2) + "/" + str(self.ano)

data = Data(5, 9, 2024)

print("Data formatada: " + data.formatar_data())
