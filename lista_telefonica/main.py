# Nesse codigo todo os.system('cls') é para limpar a tela
import os
import sys


class ListaTelefonica:
    def __init__(self, usuario):
        self.nome = usuario
        self.lista_nome = []  # Criando a lista de nome
        self.lista_telefone = []  # Criando a lista de telefone

    def cadastrar(self, lista_de_retorno):
        os.system('cls')
        self.loop = True

        # Criando minha lista com nome e telefone
        self.lista_de_retorno = lista_de_retorno
        self.nome = input('Digite o nome para cadastro: ')
        lista_de_retorno.append(self.nome)

        while self.loop:
            self.numero = input('Digite o número para cadastro: ')

            try:  # Validando o número digitado
                self.telefone = int(self.numero)
                lista_de_retorno.append(self.telefone)
                self.loop = False

            except ValueError:
                print('Digite somente números e não coloque espaçõs!')
                continue

        return lista_de_retorno

    def consultar(self):
        ...


print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')

nome = input('\nDigite seu nome: ')
usuario = ListaTelefonica(nome)
lista = []
os.system('cls')
loop = True

while loop:
    print(f'Olá, {usuario.nome}, escolha oque você deseja fazer!')
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar')
    escolha = input('>>> ')

    # Tratando o valor digitado pelo usuario
    try:
        escolha_inteiro = int(escolha)

        if escolha_inteiro == 0:
            sys.exit(0)

        elif escolha_inteiro == 1:
            os.system('cls')
            lista_principal = usuario.cadastrar(lista)
            print(lista_principal)

        elif escolha_inteiro == 2:
            os.system('cls')
            usuario.consultar()

        else:
            print('[ERRO] - Opção inválida!')
            continue

    except ValueError:
        print('[ERRO] - Digite somente inteiros!')
        continue

    except Exception:
        print('[ERRO], problema não intendificado!')
        continue
