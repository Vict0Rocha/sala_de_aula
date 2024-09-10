class Estudantes:
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

    def __repr__(self) -> str:
        return f"Matricula: {self.matricula} - Nome: {self.nome} - Idade: {self.idade}"
    

if __name__ == "__main__":
    e1 = Estudantes(111, 'Victor', 19)
    e2 = Estudantes(222, 'João', 22)
    print(repr(e1))
    print(repr(e2))
    e2.nome = 'Luana'
    e2.idade = 18
    print(repr(e2))
