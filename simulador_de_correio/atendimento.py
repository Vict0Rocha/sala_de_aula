class Atendimentos:

    def __init__(self, nome_pessoa):
        self.nome_pessoa = nome_pessoa

    def opcao(self, escolha):
        self.escolha = escolha
        print('O que você deseja fazer?')
        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Remover')

        escolha = input('Digite seua escolha: ')

        try:
            escolha_int = int(escolha)

        except ValueError:
            print('[ERRO] - Por favor, digite somente números inteiros.')
        except Exception:
            print('[ERRO] - Problema não identificado pelo sistema.')
        return escolha_int

    def fila(self, lista):
        print('Você escolheu FILA')
        n_opcao = self.opcao(self)
        # self.lista = lista
        # lista = []

        match n_opcao:
            case 1:
                print('Digite oque você deseja cadastrar')
            case 2:
                print('Sua lista é...')
            case 3:
                print('Digite o índice que dejesa revomer')
            case Exception:
                print('Opção inválida!')

    def lista(self):
        print('Você escolheu LISTA')
        self.opcao(self)
        n_opcao = self.opcao(self)

        match n_opcao:
            case 1:
                print('Digite oque você deseja cadastrar')
            case 2:
                print('Sua lista é...')
            case 3:
                print('Digite o índice que dejesa revomer')
            case Exception:
                print('Opção inválida!')

    def pilha(self):
        print('Você escolheu PILHA')
        self.opcao(self)
        n_opcao = self.opcao(self)

        match n_opcao:
            case 1:
                print('Digite oque você deseja cadastrar')
            case 2:
                print('Sua lista é...')
            case 3:
                print('Digite o índice que dejesa revomer')
            case Exception:
                print('Opção inválida!')
