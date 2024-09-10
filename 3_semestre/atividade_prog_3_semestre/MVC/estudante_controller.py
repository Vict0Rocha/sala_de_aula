from estudantes_model import Estudantes
# from estudante_view import EstudantesView


class EstudanteController:
    lista_estudantes = []

    def __init__(self, visualizacao):
        self.view = visualizacao

    def adicionar_estudante(self, matricula, nome, idade):
        novo_estudante = Estudantes(matricula, nome, idade)
        self.lista_estudantes.append(novo_estudante)

    def atualiza_nome(self, matricula, nome):
        for estudante in self.lista_estudantes:
            if matricula == estudante.matricula:
                estudante.nome = nome
                print('NOME atualizado com sucesso.')
                break

    def atualiza_idade(self, matricula, idade):
        for estudante in self.lista_estudantes:
            if matricula == estudante.matricula:
                estudante.idade = idade
                print('IDADE atualizado com sucesso.')

    def exibir_detalhes_estudantes(self):
        # EstudantesView.exibir_detalhes_estudantes(self.lista_estudantes)
        self.view.exibir_detalhes_estudantes(self.lista_estudantes)
