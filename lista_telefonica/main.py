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
        self.nome_cadastro = input('Digite o nome para cadastro: ').upper()
        # self.nome_cadastro
        lista_de_retorno.append(self.nome_cadastro)

        while self.loop:
            self.numero = input('Digite o número para cadastro: ')

            try:  # Validando o número digitado
                self.telefone = int(self.numero)
                lista_de_retorno.append(self.telefone)
                self.loop = False

            except ValueError:
                print('[ERRO] - Digite somente números e não coloque espaçõs!')
                continue

        return lista_de_retorno

    def listar(self, lista_principal):
        print('SUA LISTA DE CONTATOS\n')
        if len(lista_principal) <= 0:
            print('Nunhum contato salvo - Nada para listar\n')

        else:
            for contato in range(len(lista_principal)):
                if contato % 2 != 0:  # Pulando os índices impares
                    continue
                print(
                    f'{lista_principal[contato]}: {lista_principal[contato + 1]}')
            print()

    def consultar(self, lista_principal):
        self.nome_consulta = input('Digite o nome para consultar: ').upper()
        # self.inicio_lista = []
        self.name = int
        self.tel = int
        self.indice_numero_remover = []

        if self.nome_consulta not in lista_principal:  # Verificando se o contato está na lista
            print('Contato inecistente!\n')
        else:
            for i, contato in enumerate(lista_principal):
                if self.nome_consulta == contato:
                    # Mostrando o cotato pesquisado
                    print(f'{contato}: {lista_principal[i+1]}\n')

                    # Criando uma nova lista com o número e contato pesquisado
                    # self.inicio_lista.append(contato)
                    # self.inicio_lista.append(lista_principal[i+1])
                    self.name = i
                    self.tel = i+1

                    if 0 < self.name < len(lista_principal) and 0 < self.tel < len(lista_principal):

                        self.elemento1 = lista_principal.pop(self.name)
                        lista_principal.insert(0, self.elemento1)

                        self.elemento2 = lista_principal.pop(self.tel)
                        lista_principal.insert(1, self.elemento2)

                        # self.indice_numero_remover = lista_principal[i+1]

            print(lista_principal)
            # print(self.inicio_lista)


print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')

nome = input('\nDigite seu nome: ')
usuario = ListaTelefonica(nome)
lista = []
lista_principal = []
os.system('cls')
loop = True

while loop:
    print(f'Olá, {usuario.nome}, escolha oque você deseja fazer!')
    print('0 - Sair')
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Consultar')
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
            print()

        elif escolha_inteiro == 2:
            os.system('cls')
            usuario.listar(lista_principal)

        elif escolha_inteiro == 3:
            os.system('cls')
            usuario.consultar(lista_principal)

        else:
            print('[ERRO] - Opção inválida!')
            continue

    except ValueError:
        print('[ERRO] - Digite somente inteiros!')
        continue

    except Exception:
        print('[ERRO], problema não intendificado!')
        continue
