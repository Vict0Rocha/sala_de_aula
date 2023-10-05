class Atendimentos:

    def __init__(self, nome_pessoa):
        self.nome_pessoa = nome_pessoa

    def opcao(self, escolha, cadastro):
        self.escolha = escolha
        self.cadastro = cadastro
        print('O que você deseja fazer?')
        print('1 - Cadastrar')
        print('2 - Atender')
        print('3 - Remover')

        escolha = input('Digite seua escolha: ')
        cadastro = []

        try:
            escolha_int = int(escolha)
            match escolha:
                case 1:
                    print('Digite oque você deseja cadastrar')
                case 2:
                    pass
                case 3:
                    pass
                case Exception:
                    print('Opção inválida!')

        except ValueError:
            print('[ERRO] - Por favor, digite somente números inteiros.')
        except Exception:
            print('[ERRO] - Problema não identificado pelo sistema.')

    def fila(self, acao):
        self.acao = acao
        print('Você escolheu FILA')
        self.opcao(None, None)

    def lista(self, acao):
        self.acao = acao
        print('Você escolheu LISTA')
        self.opcao(None, None)

    def pilha(self, acao):
        self.acao = acao
        print('Você escolheu PILHA')
        self.opcao(None, None)
