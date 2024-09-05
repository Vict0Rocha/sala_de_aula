class Estudante:
    def __init__(self, matricula: int, nome: str, idade: int):
        self.__matricula = matricula
        self.__nome = nome
        self.__idade = idade

    @property
    def matricula(self):
        return self.__matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @idade.setter
    def idade(self, valor):
        self.__idade = valor
