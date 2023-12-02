# CSV
import csv


with open("teste.csv", "w", encoding="utf-8") as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=";", lineterminator="\n")
    arquivo_csv.writerow(["NOME","TELEFONE", "ENDERECO"])
    arquivo_csv.writerow(["LETICIA","123456", "RUA DARCY"])
    arquivo_csv.writerow(["DFBAHF","21482141", "AVENIDA MUNICIPAL, 235"])


with open("teste.csv", "r", encoding="utf-8") as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=";")
    arquivo_csv = list(arquivo_csv)
    for idx, linha in enumerate(arquivo_csv):
        if linha[0] == "LETICIA":
            #linha[1] = "147258"
            arquivo_csv.pop(idx)
    with open("teste.csv", "w", encoding="utf-8") as arquivo:
        arquivo_csv2 = csv.writer(arquivo, delimiter=";", lineterminator="\n")
        arquivo_csv2.writerows(arquivo_csv)


# exemplo 2


import csv


with open("teste.csv", "w", encoding="utf-8") as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=";", lineterminator="\n")
    arquivo_csv.writerow(["NOME","TELEFONE", "ENDERECO"])
    arquivo_csv.writerow(["LETICIA","123456", "RUA DARCY"])
    arquivo_csv.writerow(["DFBAHF","21482141", "AVENIDA MUNICIPAL, 235"])


with open("teste.csv", "r", encoding="utf-8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo, delimiter=";")
    arquivo_csv = list(arquivo_csv)
    print(arquivo_csv)
    for linha in arquivo_csv:
        if linha['NOME'] == "LETICIA":
            linha['TELEFONE'] = "147"
    print(arquivo_csv)


# exemplo 3
import csv


with open("teste.csv", "w", encoding="utf-8") as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=";", lineterminator="\n")
    arquivo_csv.writerow(["NOME","TELEFONE", "ENDERECO"])
    arquivo_csv.writerow(["LETICIA","123456", "RUA DARCY"])
    arquivo_csv.writerow(["DFBAHF","21482141", "AVENIDA MUNICIPAL, 235"])


with open("teste.csv", "r", encoding="utf-8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo, delimiter=";")
    arquivo_csv = list(arquivo_csv)
    print(arquivo_csv)
    for linha in arquivo_csv:
        if linha['NOME'] == "LETICIA":
            linha['TELEFONE'] = "147"
    print(arquivo_csv)

# EXEMPLO 4

import csv


with open("teste.csv", "w", encoding="utf-8") as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=";", lineterminator="\n")
    arquivo_csv.writerow(["NOME","TELEFONE", "ENDERECO"])
    arquivo_csv.writerow(["LETICIA","123456", "RUA DARCY"])
    arquivo_csv.writerow(["DFBAHF","21482141", "AVENIDA MUNICIPAL, 235"])


with open("teste.csv", "r", encoding="utf-8") as arquivo:
    arquivo_csv = csv.DictReader(arquivo, delimiter=";")
    arquivo_csv = list(arquivo_csv)
    print(arquivo_csv)
    for linha in arquivo_csv:
        if linha['NOME'] == "LETICIA":
            arquivo_csv.remove(linha)
    print(arquivo_csv)
   
    with open("teste.csv", "w", encoding="utf-8") as arquivo:
        cabecalho = ["NOME", "TELEFONE", "ENDERECO"]
        arquivo_csv2 = csv.DictWriter(arquivo,fieldnames=cabecalho,delimiter=";", lineterminator="\n")
        arquivo_csv2.writeheader()
        arquivo_csv2.writerows(arquivo_csv)
        arquivo_csv2.writerow({"NOME":"joao", "TELEFONE":"7777", "ENDERECO":"RUA DAS FLORES"})