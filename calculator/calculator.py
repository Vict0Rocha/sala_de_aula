class Calculator:
    def __init__(self, pesso, valor, cor):
        self.pesso = pesso
        self.valor = valor
        self.cor = cor

    def screen(self):
        print(f'Cor: {self.cor}')
        print(f'Pesso: {self.pesso}')
        print(f'Valor: {self.valor}')

    def soma(self, n1, n2):
        return print(f'{n1} + {n2} =  {n1 + n2}')

    def subtrair(self, n1, n2):
        return print(f'{n1} - {n2} =  {n1 - n2}')

    def multiplicar(self, n1, n2):
        return print(f'{n1} * {n2} =  {n1 * n2}')

    def dividir(self, n1, n2):
        return print(f'{n1} / {n2} = {n1/n2}')

    def fatorial(self, numero, numero2):
        self.numero = numero
        resultado = 1
        count = 1
        while count <= numero:
            resultado *= count
            count += 1

        self.numero2 = numero2
        resultado2 = 1
        count2 = 1
        while count2 <= numero2:
            resultado2 *= count2
            count2 += 1

        return print(f'O fatorial de {numero} é {resultado}\n \
O fatorial de {numero2} é {resultado2}')

    def potencia(self, n1, n2):
        return print(f'A potencia de {n1} sobre {n2} é: {n1**n2}')
