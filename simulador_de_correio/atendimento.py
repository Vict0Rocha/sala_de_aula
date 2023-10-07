import os
import sys


class Atendimentos:

    def __init__(self, nome_pessoa):
        self.nome_pessoa = nome_pessoa

    def opcao(self, escolha):
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
            n_opcao = self.opcao(self)

            match n_opcao:
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

                    os.system('cls')
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

    def lista(self):
        print('Você escolheu LISTA')
        n_opcao = self.opcao(self)

    def pilha(self):
        print('Você escolheu PILHA')
        n_opcao = self.opcao(self)
