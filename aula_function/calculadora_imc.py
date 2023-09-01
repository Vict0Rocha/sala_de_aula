from func_imc import imc, nome #Importando a função de outro arquivo
import os

condicao = True

while condicao == True:
    nome_atual = nome()
    print(f'Olá {nome_atual}, seu IMC é: {imc()}')

    print('Deseja carcular novemente? ')

    escolha = input('[S]im [N]ão\n').upper()

    if escolha == 'S':
        continue
    elif escolha == 'N':
        condicao = False
    else:
        os.system('cls')
        continue