import csv

class Lista_Telefonica:
    def __init__(self, nome_arquivo, nome, telefone):
        self.nome_arquivo = nome_arquivo
        self.nome = nome
        self.telefone = telefone

    def cadastrar(self):
        with open(self.nome_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo_csv = csv.writer(arquivo, delimiter=';', lineterminator="\n")
            arquivo_csv.writerow(["NOME", "TELEFONE", 'ENDEREÇO'])

    def listar(self):
        pass

    def consultar(self):
        pass

    def editar(self):
        pass

    def excluir(self):
        pass