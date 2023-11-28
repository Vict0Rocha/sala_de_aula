import csv

with open('teste.csv', 'w', encoding='utf-8') as arquivo:
    arquivo_csv = csv.writer(arquivo, delimiter=';', lineterminator='\n')
    arquivo_csv.writerow(['NOME', 'TELEFONE', 'ENDEREÇO'])
    arquivo_csv.writerow(['Valber', '5555', 'Rua C, casa 2'])
    arquivo_csv.writerow(['Victor', '2222', 'Rua A, casa 10'])
    arquivo_csv.writerow(['Maria', '7777', 'Rua AWS, casa 58'])
    

with open('teste.csv', 'r', encoding='utf-8') as arquivo:
    arquivo_csv = csv.DictReader(arquivo, delimiter=';')
    arquivo_csv = list(arquivo_csv)
    print(arquivo_csv)
    for linha in arquivo_csv:
        print(linha['NOME'])
        if linha['NOME'] == 'Valber':
            arquivo_csv.remove(linha)

with open('teste.csv', 'w', encoding='utf-8') as arquivo:
    cabecalho = ['NOME', 'TELEFONE', 'ENDEREÇO']
    arquivo_csv2 = csv.DictWriter(arquivo, fieldnames=cabecalho, delimiter=';', lineterminator='\n')
    arquivo_csv2.writeheader()
    arquivo_csv2.writerows(arquivo_csv)
    arquivo_csv2.writerows({'NOME':'LETICIA', 'TELEFONE':'9999', 'ENDEREÇO':'ADFASD,AFSD'})
            
            
            #inha['TELEFONE'] = '10000' # Alterando o valor do telefone
        #print(arquivo_csv)
    #for index, linha in enumerate(arquivo_csv):
     #   if linha[0] == 'Valber': 
      #      pass
            #linha[1] = '1111' #Alterando o valor do vetor pela posição do vetor 
            #arquivo_csv.pop(index)

    #with open('teste.csv', 'w', encoding='utf-8') as arquivo:
     #   arquivo_csv2 = csv.writer(arquivo, delimiter=';', lineterminator='\n')
      #  arquivo_csv2.writerows(arquivo_csv)


