
class Aluno:
    def __init__(self, nome, nota):

        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        
        if self.nota >= 7:
            print('O aluno ' + self.nome + ' está aprovado!')
        else:
            print('O aluno ' + self.nome + ' está reprovado.')


aluno1 = Aluno("João", 8)
aluno2 = Aluno("Maria", 5)

aluno1.verificar_aprovacao()
aluno2.verificar_aprovacao()


nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

aluno = Aluno(nome, nota)

aluno.verificar_aprovacao()


