
class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(contato)
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if len(self.contatos) == 0:
            print("A agenda está vazia.")
        else:
            print("Contatos na agenda:")
            for contato in self.contatos:
                print("Nome: " + contato["nome"] + " | Telefone: " + contato["telefone"])

agenda = Agenda()
agenda.adicionar_contato("Eduarda", "1234-5678")
agenda.adicionar_contato("Mario", "9876-5432")

agenda.listar_contatos()
