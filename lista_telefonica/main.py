import os


class Telefone:
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
usuario = Telefone(nome)
os.system('cls')

print(f'Olá, {usuario.nome}, escolha oque você deseja fazer!')
print('1 - Cadastrar')
print('2 - Listar')
escolha = input('<<< ')

try:
    escolha_inteiro = int(escolha)

except ValueError:
    print('[ERRO] - Digite somente inteiros!')

except Exception:
    print('[ERRO], problema não intendificado!')
