from lista_de_telefones import Lista_Telefonica
import sys
# import os

print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')
print('')

while True:
    print('Digite o número corespondente do que você deseja?')
    print('\n1 - CADASTRAR')
    print('2 - LISTAR')
    print('3 - CONSULTAR')
    print('4 - EDITAR')
    print('5 - EXCLUIR')
    print('6 - SAIR')
    escolha = input('<<< ')

    # Convertendo e verificando se o valor digitado é um número inteiro.
    try:
        escolha_int = int(escolha)
        match escolha_int:
            case 1:
                print('Você escolheu CADASTAR')
                continue

            case 2:       
                print('Você escolheu LISTAR')
                continue

            case 3:
                print('Você escolheu CONSULTAR')
                continue

            case 4:
                print('Você escolheu EDITAR')
                continue

            case 5:
                print('Você escolheu EXCLUIR')
                continue
                
            case 6:
                sys.exit(0) #Finalizando o programa.

            case Exception:
                print('[ERRO] - O valor digitado, não coresponde a NENHUMA OPÇÃO.')

    except ValueError:
        print('[ERRO] - Por favor, digite somente números INTEIROS.')
        continue
    except Exception:
        print('[ERRO] - Porblema não identificado pelo sistema.')

