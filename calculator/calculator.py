class Calculator:
    def __init__(self, pesso, valor, cor):
        self.pesso = pesso
        self.valor = valor
        self.cor = cor

    def screen(self):
        print('O estilo da calculadora é...')
        print(f'Cor: {self.cor}')
        print(f'Pesso: {self.pesso}')
        print(f'Valor: {self.valor}')

    def soma(self, n1, n2):
        return print(f'{n1} + {n2} =  {n1 + n2}')

    def subtrair(self, n1, n2):
        return print(f'{n1} - {n2} =  {n1 - n2}')

    def multiplicar(self, n1, n2):
        return print(f'{n1} * {n2} =  {n1 * n2}')
