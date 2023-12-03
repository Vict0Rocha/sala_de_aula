import csv

class Lista_Telefonica:
    def __init__(self, nome_arquivo, nome, telefone, endereco):
        self.nome_arquivo = nome_arquivo
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def cadastrar(self):
        with open(self.nome_arquivo, 'a', encoding='utf-8') as arquivo:
            cabecalho = (["NOME", "TELEFONE", 'ENDEREÇO'])
            arquivo_csv = csv.DictWriter(arquivo, fieldnames=cabecalho, delimiter=';', lineterminator="\n")
            
            # Verificando se o arquivo está vazio, e escrevendo o cabeçalho
            if arquivo.tell() == 0:
                arquivo_csv.writeheader()

            # Escrevendo a nova linha do meu arquivo
            arquivo_csv.writerow({'NOME':self.nome, 'TELEFONE':self.telefone, 'ENDEREÇO':self.endereco})


    def listar(self):
        pass

    def consultar(self):
        pass

    def editar(self):
        pass

    def excluir(self):
        pass