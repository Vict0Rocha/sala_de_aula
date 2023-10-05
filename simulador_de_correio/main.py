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
        pessoa.lista(1)
    case 'F':
        pessoa.fila(None, None)
    case 'P':
        pessoa.pilha(1)
    case Exception:
        print('Opção inválida!')
