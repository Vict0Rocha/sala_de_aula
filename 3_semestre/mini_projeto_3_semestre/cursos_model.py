class Curso:
    def __init__(self, codigo, nome, duracao, professor):
        self._codigo = codigo
        self._nome = nome
        self._duracao = duracao
        self._professor = professor

    # Getters e Setters (Encapsulamento)
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def duracao(self):
        return self._duracao

    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao

    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, professor):
        self._professor = professor

    def __str__(self):
        return f"Curso: {self._nome} - Código: {self._codigo}, Duração: {self._duracao} meses, Professor: {self._professor.nome}"


class Professor:
    def __init__(self, nome, especialidade):
        self._nome = nome
        self._especialidade = especialidade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

    def __str__(self):
        return f"{self._nome} (Especialidade: {self._especialidade})"
