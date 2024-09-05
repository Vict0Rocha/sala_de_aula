# Questão 1
# Sistema de Gerenciamento de Funcionários com Herança e Polimorfismo

from abc import ABC, abstractmethod


class Funcionario(ABC):
    def __init__(self, nome: str, salario_base: float):
        self.nome = nome
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self) -> float: ...


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, salario_base: float, vendas: float,
                 taxa_comissao: float):
        super().__init__(nome, salario_base)
        self.vendas = vendas
        self.taxa_comissao = taxa_comissao

    def calcular_salario(self) -> float:
        comissao = self.vendas * self.taxa_comissao
        return self.salario_base + comissao


class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, 0)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        total_ganho = self.horas_trabalhadas * self.valor_hora
        return total_ganho


f_comissionado = FuncionarioComissionado("Victor", 1420.0, 2000.0, 0.10)
print("Salario do funcionário COMISSIONADO:",
      f_comissionado.calcular_salario())


f_horista = FuncionarioHorista("João", 8, 20)
print("Salario do funcionáro HORISTA:",
      f_horista.calcular_salario())
