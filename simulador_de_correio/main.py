from atendimento import Atendimentos
import os

print(10*'-')
print(' CORREIO ')
print(10*'-')

nome = input('Digite seu nome: ')
pessoa = Atendimentos(nome)

print(f'Olá, {pessoa.nome_pessoa}, como você quer ser atendido?')
print('[L]- Lista [F]- Fila [P]- Pilha')
esccolha = input('<<< ').upper()

match esccolha:
    case 'L':
        pessoa.lista()
    case 'F':
        pessoa.fila()
    case 'P':
        pessoa.pilha()
    case Exception:
        print('Opção inválida!')
