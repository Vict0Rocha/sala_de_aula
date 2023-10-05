class Atendimentos:

    def __init__(self, nome_pessoa):
        self.nome_pessoa = nome_pessoa

    def fila(self, acao, escolha):
        self.acao = acao
        self.escolha = escolha
        print('O que você deseja fazer?')
        print('1 - Cadastrar')
        print('2 - Atender')
        print('3 - Remover')

        escolha = input('Digite seua escolha: ')

        try:
            escolha_int = int(escolha)
            print('OK')
        except ValueError:
            print('[ERRO] - Por favor, digite somente inteiros.')
        except Exception:
            print('[ERRO] - Problema não identificado pelo sistema.')

    def lista(self, acao):
        self.acao = acao
        print('Lista')

    def pilha(self, acao):
        self.acao = acao
        print('Pilha')
