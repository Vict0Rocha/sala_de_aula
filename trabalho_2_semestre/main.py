from lista_de_telefones import Lista_Telefonica
import os
# import sys

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
    escolha = input('>>> ')

    # Convertendo e verificando se o valor digitado é um número inteiro.
    try:
        escolha_int = int(escolha)
        match escolha_int: # Verificando a escolha do usuario.
            case 1:
                print('Você escolheu CADASTAR\n')
                nome =  input('Digite o NOME: ').upper()
                telefone =  input('Digite o TELEFONE: ')

                # Verificando se o telefone tem somente números
                try:
                    telefone_int = int(telefone)
                except ValueError:
                    print('[ERRO] - Por favor, digite SOMENTE NÚMEROS')
                    continue

                endereco =  input('Digite o ENDEREÇO: ').upper()
                lista_telefonica = Lista_Telefonica('trabalho_2_semestre\contatos.csv', nome, telefone_int, endereco)
                lista_telefonica.cadastrar()

            case 2:
                print('Você escolheu LISTAR')
                Lista_Telefonica.listar('trabalho_2_semestre\contatos.csv')

            case 3:
                print('Você escolheu CONSULTAR')
                nome_consulta = input('Digite o nome para consultar: ').upper()
                Lista_Telefonica.consultar('trabalho_2_semestre\contatos.csv', nome_consulta)

            case 4:
                print('Você escolheu EDITAR')
                print('Digite o nome que você deseja realizar alguma alteração')
                nome_alteracao = input('>>> ').upper()
                Lista_Telefonica.editar('trabalho_2_semestre\contatos.csv', nome_alteracao)

            case 5:
                print('Você escolheu EXCLUIR')
                continue

            case 6:
                # sys.exit(0) #Finalizando o programa.
                break

            case Exception:
                print('[ERRO] - O valor digitado, não coresponde a NENHUMA OPÇÃO.')

    except ValueError:
        print('[ERRO] - Por favor, digite somente números INTEIROS.')
        continue
    # except Exception:
    #     print('[ERRO] - Porblema não identificado pelo sistema.')

