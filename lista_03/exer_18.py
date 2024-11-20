
class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_horario(self):
        return str(self.hora).zfill(2) + ":" + str(self.minuto).zfill(2)

relogio = Relogio(9, 5, 30)
print("Horário: " + relogio.exibir_horario())
