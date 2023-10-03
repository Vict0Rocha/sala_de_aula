
from calculadora_padrao import CaculatorPadrao

class CalculatorTop(CaculatorPadrao):
    def __init__(self, pesso, valor, cor):
       super().__init__(pesso, valor, cor)

    def fatorial(self, num1):

        if num1 == 1:
          return num1
        return num1 * self.fatorial(num1 - 1) 
        

    def potencia(self, n1, n2):
        return print(f'A potencia de {n1} sobre {n2} é: {n1**n2}')