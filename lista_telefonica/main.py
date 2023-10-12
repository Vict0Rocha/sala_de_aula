import os
# Nesse codigo todo os.system('cls') é para limpar a tela


class ListaTelefonica:
    def __init__(self, usuario):
        self.nome = usuario
        self.lista_nome = []  # Criando a lista de nome
        self.lista_telefone = []  # Criando a lista de telefone

    def cadastrar(self):
        os.system('cls')
        self.lista_principal = []  # Criando minha lista com nome e telefone
        self.nome = input('Digite o nome para cadastro: ')
        self.lista_principal.append(self.nome)
        self.numero = input('Digite o número para cadastro: ')

        try:  # Validando o número digitado
            self.telefone = int(self.numero)
            self.lista_principal.append(self.telefone)

        except ValueError:
            print('Digite somente números e não coloque espaçõs!')

        return self.lista_principal

    def listar(self):
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

# Tratando o valor digitado pelo usuario
try:
    escolha_inteiro = int(escolha)

    if escolha_inteiro == 1:
        os.system('cls')
        usuario.cadastrar()

    elif escolha_inteiro == 2:
        os.system('cls')
        usuario.listar()

    else:
        print('[ERRO] - Opção inválida!')

except ValueError:
    print('[ERRO] - Digite somente inteiros!')

except Exception:
    # print(NameError)
    print('[ERRO], problema não intendificado!')
