''' Questão 3
Sistema de gerenciamento de estudantes com MVC e atributos de classe
'''


class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"Estudante nome='{self.nome}', idade={self.idade}"


class View:
    def exibir_detalhes_estudantes(self, estudantes):
        for estudante in estudantes:
            print(estudante)


# Exemplo de uso
estudantes = [Estudante("Alice", 20), Estudante("Bob", 22)]
view = View()
view.exibir_detalhes_estudantes(estudantes)
