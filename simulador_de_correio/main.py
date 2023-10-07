from atendimento import Atendimentos
import os

print(10*'-')
print(' CORREIO ')
print(10*'-')

nome = input('Digite seu nome: ')
pessoa = Atendimentos(nome)

print(f'Olá, {pessoa.nome_pessoa}, como você quer ser atendido?')
print(' [L]- Lista\n [F]- Fila\n [P]- Pilha')
esccolha = input('<<< ').upper()

match esccolha:
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
