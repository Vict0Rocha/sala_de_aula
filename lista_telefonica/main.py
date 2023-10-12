import os


class ListaTelefonica:
    def __init__(self, usuario):
        self.nome = usuario
        self.lista_nome = []
        self.lista_telefone = []

    def cadastrar(self):
        ...


print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')

nome = input('\nDigite seu nome: ')
usuario = ListaTelefonica(nome)
os.system('cls')

print(f'Olá, {usuario.nome}, escolha oque você deseja fazer!')
print('1 - Cadastrar')
print('2 - Listar')
escolha = input('<<< ')

try:
    escolha_inteiro = int(escolha)
    if escolha_inteiro == 1:
        print('CADASTRADO')

    elif escolha_inteiro == 2:
        print('LISTANDO')
    else:
        print('[ERRO] - Opção inválida!')

except ValueError:
    print('[ERRO] - Digite somente inteiros!')

except Exception:
    print('[ERRO], problema não intendificado!')
