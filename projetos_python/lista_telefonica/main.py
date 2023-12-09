from lista_telefonica import ListaTelefonica
import sys
import os

'''
Um sistema que simula uma lista telefônica, podendo cadastrar um 
nome e telefone, listar todos os contatos salvos e pesquisar um 
contato pelo nome, ao pesquisar o contato, é feito um  cache, 
pegando o nome e telefone do final da lista e colocando no  inicio.
'''


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
            # print(lista_principal)
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
        print('[ERRO] - Digite somente números inteiros!')
        continue

    except Exception:
        print('[ERRO], problema não intendificado!')
        continue
