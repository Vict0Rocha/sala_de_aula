from calculator import Calculator
import os

calculator_padrao = Calculator('2Kg', 'R$5.00', 'Roxo')
calculator_top = Calculator('500gm', 'R$2.000', 'Rosa')

print('Digie 1 - Calculadora Padrão')
print('Digie 2 - Calculadora Top')

opcao = input('Digite qual calculadora você que usar: ')


if opcao == 1:
    os.system('cls')
    print('As informações da calculadora escolhida é... ')
    calculator_padrao.screen()
    print()
    n1 = float(input('Digite o 1° valor: '))
    n2 = float(input('Digite o 2° valor: '))
    print('O resultados possivel são...')
    calculator_padrao.soma(n1, n2)
    calculator_padrao.subtrair(n1, n2)
    calculator_padrao.multiplicar(n1, n2)
    calculator_padrao.dividir(n1, n2)

elif opcao == 2:
    os.system('cls')
    print('As informações da calculadora escolhida é... ')
    calculator_top.screen()
    print()
    n1 = float(input('Digite o 1° valor: '))
    n2 = float(input('Digite o 2° valor: '))
    print('O resultados possivel são...')
    calculator_top.soma(n1, n2)
    calculator_top.subtrair(n1, n2)
    calculator_top.multiplicar(n1, n2)
    calculator_top.dividir(n1, n2)
    calculator_top.fatorial(n1, n2)
    calculator_top.potencia(n1, n2)

else:
    print('Opção invalida!')