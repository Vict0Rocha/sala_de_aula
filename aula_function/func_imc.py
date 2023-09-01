def imc():
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))
    resultado = peso / (altura**2)
    return resultado

def nome():
    return input('Digite seu nome: ')