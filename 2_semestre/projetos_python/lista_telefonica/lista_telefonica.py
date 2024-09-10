# Nesse codigo todo os.system('cls') é para limpar a tela
import os


class ListaTelefonica:
    def __init__(self, usuario):
        self.nome = usuario
        self.lista_nome = []  # Criando a lista de nome
        self.lista_telefone = []  # Criando a lista de telefone

    # A lista de retorno é a mesma que a lista principal
    def cadastrar(self, lista_de_retorno):
        os.system('cls')
        self.loop = True

        # Criando minha lista com nome e telefone
        self.lista_de_retorno = lista_de_retorno
        self.nome_cadastro = input('Digite o nome para cadastro: ').upper()
        # self.nome_cadastro
        lista_de_retorno.append(self.nome_cadastro)

        # Enquando não digitar um número de telefone válido, não sei do loop
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
        # Verificando o tamanha da minha lista, caso não tenha nada
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
        self.indice_numero_remover = []

        if self.nome_consulta not in lista_principal:  # Verificando se o contato está na lista
            print('Contato inecistente!\n')
        else:
            # Percorrendo os indices o valores da minha lista de contatos
            for i, contato in enumerate(lista_principal):
                if self.nome_consulta == contato:
                    # Mostrando o cotato pesquisado
                    print(f'{contato}: {lista_principal[i+1]}\n')

                    self.name = i  # Indice 1
                    self.tel = i+1  # Indice 2

                    # Verificando se o nome escolhido já não está no inicio da lista
                    if 0 < self.name < len(lista_principal) and 0 < self.tel < len(lista_principal):

                        # Deletando o nome da lista e inserindo no inicio
                        self.elemento1 = lista_principal.pop(self.name)
                        lista_principal.insert(0, self.elemento1)
                        # Deletando o telefone da lista e inserindo no inicio
                        self.elemento2 = lista_principal.pop(self.tel)
                        lista_principal.insert(1, self.elemento2)
