# Nome do aquivo = comando; open para abrir
# R - Modo de leitura - Caso não exista, vai dar erro
# W - Escrita - Caso não exista ele cria um novo arquivo - Sobescreve um arquivo
# A - Anexar - Aciciona no final do arquivo


# arquivo = open('texto.txt', 'w', encoding='utf-8')
# # arquivo = open('texto.html', 'w', encoding='utf-8')
# arquivo.write('Meu nome é Leticia 7')


# arquivo = open('texto.txt', 'a', encoding='utf-8')
# arquivo.write('\nSegunda linha')
# arquivo.write('\nValber')
# arquivo.write('\nLeticia')
# arquivo.write('\nVilma')
# arquivo.write('\nHenrique\n')


# lista = ['Valber\n', 'Letica\n', 'Vilma\n', 'Henrique\n', 'Victor\n']
# arquivo.writelines(lista) # Para escrever em lista


# arquivo.write(' \n')


# for nome in lista:
#     arquivo.write(nome)


# arquivo.close()


with open('texto.txt', 'w', encoding='utf-8') as x:
    # lista = ['Nome: Vitão\n', 'Telefone: 1111\n', 'Endereço: logo ali']
    # lista = ['Nome: Vitão\n', 'Telefone: 1111\n', 'Endereço: logo ali']
    # lista = ['Nome: Vitão', ' Telefone: 1111', ' Endereço: logo ali\n',]
    # lista2 = ['Nome: Henrique', 'Telefone: 222', ' Endereço: Bem longe\n',]
    # lista3 =['Nome: Valber', ' Telefone: 3333', ' Endereço: Fora de casa\n',]
    # x.writelines(lista)
    # x.writelines(lista2)
    # x.writelines(lista3)
    # # a = 0 / 2
    x.write('Nome: Vitão\n')
    x.write('Telefone: 1111\n')
    x.write('Endereço: logo ali\n')


    x.write('\nNome: Valber\n')
    x.write('Telefone: 2222\n')
    x.write('Endereço: Logo ali\n')


    x.write('\nNome: Henrique\n')
    x.write('Telefone: 3333\n')
    x.write('Endereço: Fora de casa\n')

vet = []
p = 1


with open('texto.txt', 'r', encoding='utf-8') as x:

    # print(x.readlines())
    # print(x.readlines())
    # print(x.readline(2))
    # print(x.tell())
    # print(x.read())
    # print(x.tell()) # Conta os carecteres do arquivo
    # x.seek(59) # Deixa o cursor na linha desejada
    # print(x.tell())
    # for nome in lista:
    # print(x.readlines())
    for linha in x.readlines():
        if 'Telefone: ' in linha:
            vet.append(linha)


print(vet[p])