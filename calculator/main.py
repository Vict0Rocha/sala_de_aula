from calculator_padrao import CaculatorPadrao
from calculator_top import CalculatorTop
import os

print('Digie 1 - Calculadora Padrão')
print('Digie 2 - Calculadora Top')

opcao = int(input('Digite qual calculadora você que usar: '))

os.system('cls')

n1 = float(input('Digie o 1° valor: '))
n2 = float(input('Digie o 2° valor: '))

if opcao == 1:
    os.system('cls')
    calculator_padrao = CaculatorPadrao('2Kg', 'R$5.00', 'Roxo')
    print('As informações da calculadora escolhida é... ')
    calculator_padrao.screen()
    print()
    # print('A qui você tem as seguintes opções...')
    # print('+ - * / ')
    # operador_escolha = input('Digite qual operação você quer fazer: ')
    calculator_padrao.soma(n1, n2)
    calculator_padrao.subtrair(n1, n2)
    calculator_padrao.multiplicar(n1, n2)
    calculator_padrao.dividir(n1, n2)
    # match(operador_escolha):
    #     case '+':
    #         calculator_padrao.soma(n1, n2)
    #     case '-':
    #         calculator_padrao.subtrair(n1, n2)
    #     case '*':
    #         calculator_padrao.multiplicar(n1, n2)
    #     case '/':
    #         calculator_padrao.dividir(n1, n2)
    #     case '!=':
    #         ...
    #     case '**':
    #        ...

elif opcao == 2:
    calculator_top = CalculatorTop('500gm', 'R$2.000', 'Rosa')
    os.system('cls')
    print('As informações da calculadora escolhida é... ')
    calculator_top.screen()
    print()
    print('O resultados possivel são...')
    calculator_top.soma(n1, n2)
    calculator_top.subtrair(n1, n2)
    calculator_top.multiplicar(n1, n2)
    calculator_top.dividir(n1, n2)
    calculator_top.fatorial(n1)
    calculator_top.potencia(n1, n2)

else:
    print('Opção invalida!')
