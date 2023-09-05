import os

def calcula_imc(peso, altura):
    return peso / altura**2

def imprime_imc():
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sau altura: '))
    imc = calcula_imc(peso, altura)
    print(f'Olá, {nome}, seu IMC é: {imc:.2f}')

condicao = True

while condicao:
    # os.system('cls')
    imprime_imc()


