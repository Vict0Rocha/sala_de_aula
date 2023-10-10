import os  # Usado para limpar o terminar
import sys  # Usado para finalizar o programa


class Atendimentos:

    def __init__(self, nome_pessoa):
        self.nome_pessoa = nome_pessoa

    def opcao(self, escolha):
        # Função usada somente como um menu, para mostrar as possibilidades
        self.escolha = escolha
        validacao = True
        print('O que você deseja fazer?')
        print('0 - Finalizar o programa')
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Remover')

        while validacao == True:
            escolha = input('Digite sua escolha: ')
            try:
                escolha_int = int(escolha)
                validacao = False
            except ValueError:
                print('[ERRO] - Por favor, digite somente números inteiros.')
                continue
            except Exception:
                print('[ERRO] - Problema não identificado pelo sistema.')
                continue
            return escolha_int

    def fila(self):
        print('Você escolheu FILA')
        condicao = True
        lista = []
        while condicao == True:
            # Atribuindo o retorno da função opção para outra variavel
            n_opcao = self.opcao(self)

            match n_opcao:  # Verificando o retorno recebido
                case 0:
                    sys.exit(0)
                case 1:
                    os.system('cls')
                    print('Digite oque você deseja cadastrar')
                    item_cadastro = input('<<< ')
                    lista.append(item_cadastro)

                case 2:
                    os.system('cls')
                    if len(lista) <= 0:
                        print('Nada para lista')
                    # Percorrendo e enumerando cada item da lista adicionado
                    for i, item_cadastro in enumerate(lista):
                        print(f'{i}) {item_cadastro}')
                    print('')

                case 3:
                    lista.pop(0)

                case Exception:
                    print('Opção inválida!')
                    continue

    def lista(self):
        print('Você escolheu LISTA')
        condicao = True
        lista = []
        while condicao == True:
            # Atribuindo o retorno da função opção para outra variavel
            n_opcao = self.opcao(self)

            match n_opcao:
                # Verificando o retorno recebido
                case 0:
                    sys.exit(0)
                case 1:
                    os.system('cls')
                    indice_item = input('Digite o índice que você deseja colocar seu item: ')
                    try:
                        indice_item = int(indice_item)
                        print('Digite oque você deseja cadastrar')
                        item_cadastro = input('<<< ')
                        lista.insert(indice_item, item_cadastro)
                    except ValueError:
                        print('[ERRO] - Digite somente números')
                    

                case 2:
                    os.system('cls')
                    if len(lista) <= 0:
                        print('Nada para lista')
                    # Percorrendo e enumerando cada item da lista adicionado
                    for i, item_cadastro in enumerate(lista):
                        print(f'{i}) {item_cadastro}')
                    print('')

                case 3:
                    print('Digite o índice que dejesa revomer')
                    indice_digitado = input('<<< ')

                    try:
                        indice_remover = int(indice_digitado)
                        del lista[indice_remover]
                    except ValueError:
                        print('[ERRO] - Por favor, digite somente inteiros.')
                        continue
                    except IndexError:
                        print('[ERRO] - Índice não existe na sua lista.')
                        continue

                case Exception:
                    print('Opção inválida!')
                    continue

    def pilha(self):
        print('Você escolheu PILHA')
        condicao = True
        lista = []
        while condicao == True:
            # Atribuindo o retorno da função opção para outra variavel
            n_opcao = self.opcao(self)

            match n_opcao:
                # Verificando o retorno recebido
                case 0:
                    sys.exit(0)
                case 1:
                    os.system('cls')
                    print('Digite oque você deseja cadastrar')
                    item_cadastro = input('<<< ')
                    lista.append(item_cadastro)

                case 2:
                    os.system('cls')
                    if len(lista) <= 0:
                        print('Nada para lista')

                    # Percorrendo e enumerando cada item da lista adicionado
                    for i, item_cadastro in enumerate(lista):
                        print(f'{i}) {item_cadastro}')
                    print('')

                case 3:
                    lista.pop()

                case Exception:
                    print('Opção inválida!')
                    continue
