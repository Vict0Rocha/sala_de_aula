from calculator import Calculator

calculator_padrao = Calculator('2Kg', 'R$5.00', 'Roxo')
calculator_top = Calculator('500gm', 'R$2.000', 'Rosa')

print('Digie 1 - Calculadora Padrão')
print('Digie 2 - Calculadora Top')

opcao = int(input('Digite qual calculadora vc que usar: '))

if opcao == 1:
    print('\nAs informações da calculadora escolhida é... ')
    calculator_padrao.screen()

elif opcao == 2:
    print('\nAs informações da calculadora escolhida é... ')
    calculator_top.screen()
else:
    print('Opção invalida!')


# calculator_padrao.soma(5, 5)
# print(calculator_padrao.subtrair(10, 5))
# print(calculator_padrao.multiplicar(3, 5))

# calculator_padrao.screen()
# print(20*'-')
# calculator_top.screen()
