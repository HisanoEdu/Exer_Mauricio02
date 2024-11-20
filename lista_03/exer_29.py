
class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def iniciar_jogo(self):
        print("Iniciando o jogo " + self.nome + "...")

    def registrar_pontuacao(self, pontos):
        self.pontuacao += pontos
        print("Pontuação registrada: " + str(pontos))

    def exibir_pontuacao(self):
        print("Pontuação atual: " + str(self.pontuacao))

jogo = Jogo("Super Mario")

jogo.iniciar_jogo()
jogo.registrar_pontuacao(100)
jogo.registrar_pontuacao(50)
jogo.exibir_pontuacao()
