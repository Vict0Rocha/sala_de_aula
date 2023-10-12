class Funcao:
    def __init__(self):
        self.lista1 = ['Victor', 'João', 'Valber', 'Thiago', 'Pedro', 'Leticia', 'Ana', 'Luana', 'Daniel', 'Matheus']

    def copiar(self, lista1, lista2):
        self.lista1 = self.lista1
        self.lista2 = lista2
        
        lista2 = lista1[:]

        return lista2
    
    def concatenar(self):
        ...

    def intercalar(self):
        ...