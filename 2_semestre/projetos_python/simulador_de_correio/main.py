'''
Simulador de correiro - O usuario escolhe a forma no qual deseja ser atendido 
Em seguida ele pode escolher oque deseja fazer para gerenciar seus items 
Os items são armazenados em uma lista, no qual ele pode - adicionar; listar e remover items
'''

from atendimento import Atendimentos
import os

print(10*'-')
print(' CORREIO ')
print(10*'-')

nome = input('Digite seu nome: ')
pessoa = Atendimentos(nome)

print(f'Olá, {pessoa.nome_pessoa}, como você quer ser atendido?')
print(' [L]- Lista\n [F]- Fila\n [P]- Pilha')
# Recebendo a escolha e deixando tudo maísculo
esccolha = input('<<< ').upper()

match esccolha:
    # Verificando oque foi escolhido pelo usuario
    case 'L':
        os.system('cls')
        pessoa.lista()
    case 'F':
        os.system('cls')
        pessoa.fila()
    case 'P':
        os.system('cls')
        pessoa.pilha()
    case Exception:
        print('Opção inválida!')
