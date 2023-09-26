# ----------------------------------------
# cabelo - olho - altura - sexo - ATRIBUTOS
# ----------------------------------------
# falar - andar - METODOS

class Pessoa:
    def __init__(self, nome, olho, cabelo, altura, sexo):
        self.nome = nome
        self.olho = olho
        self.cabelo = cabelo
        self.altura = altura
        self.sexo = sexo

    def andar(self):
        print('Estou ANDANDO')

    def falar(self):
        print('Estou FALANDO')
