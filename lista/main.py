class Vetor:
    def __init__(self):
        self.lista1 = ['Victor', 'João', 'Valber', 'Thiago', 'Pedro', 'Leticia', 'Ana', 'Luana', 'Daniel', 'Matheus']

    def copiar(self, lista2):
        for nome in self.lista1:
            lista2.append(nome)
        return lista2
    
    def concatenar(self, lista_concatenada):
        vet = []
        vet = self.copiar(vet)
        for posicao in self.lista1:
            lista_concatenada.append(posicao)

        for posicao in vet:
            lista_concatenada.append(posicao)

        return print(lista_concatenada)
        

    def intercalar(self, lista4):
        self.lista4 = lista4
        vet2 = []
        vet2 = self.copiar(vet2)
        teste = self.lista1
        # vet = []
        # vet = self.concatenar(vet)
        
        for nome in range(len(vet2)):
            lista4.append(teste[nome])
            lista4.append(vet2[nome])
        return print(lista4)

lista = Vetor()
lista_juntada = []
lista.copiar(lista_juntada)
print(lista_juntada)
print('-'*30)
list_concatena = []
lista.concatenar(list_concatena)
print('-'*30)
concatenar = []
lista.intercalar(concatenar)

# lista3 = []
# lista.concatenar(lista3)
# print('-'*30)
# lista_concatenada = []
# lista.concatenar(lista_concatenada)
# print(lista.concatenar(lista_concatenada))