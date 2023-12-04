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

    @staticmethod
    def listar(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            arquivo_csv = csv.DictReader(arquivo, delimiter=';')
            for linha in arquivo_csv:
                print(linha)
            return [linha for linha in arquivo_csv]

    @staticmethod
    def consultar(nome_arquivo, nome_consulta):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            arquivo_csv = csv.DictReader(arquivo, delimiter=';')
            for linha in arquivo_csv:
                if nome_consulta == linha['NOME']:
                    print(linha)

    @staticmethod
    def editar(nome_arquivo, nome_alteracao):
        linhas = []

        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            arquivo_csv = csv.DictReader(arquivo, delimiter=';')
            for linha in arquivo_csv:
                linhas.append(linha)

        print(linhas)
        for linha in linhas:
            if nome_alteracao == linha['NOME']: # Procurando o quem o usuario deseja alterar 
                print('Digite o índice do campo que deseja alterar.')
                print('0 - NOME')
                print('1 - TELEFONE')
                print('2 - ENDEREÇO')
                campo_alteracao = int(input('>>> '))
                print('Digite o novo valor')
                novo_valor = input('>>> ')
                linha[campo_alteracao] = novo_valor

        with open(nome_arquivo, 'w', encoding='utf-8', newline='') as arquivo:
            cabecalho = ["NOME", "TELEFONE", 'ENDEREÇO']
            arquivo_csv = csv.DictWriter(arquivo, fieldnames=cabecalho, delimiter=';', lineterminator="\n")
            arquivo_csv.writeheader()
            arquivo_csv.writerows(linhas)

    # @staticmethod
    # def ler_arquivo():
    #     pass

    # @staticmethod
    # def escrever_arquivo():
    #     pass

    # @staticmethod
    # def adicionar_arquivo():
    #     pass


    # @staticmethod
    def excluir(self):
        pass