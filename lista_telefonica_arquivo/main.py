print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')
print('')

nome_do_arquivo = 'lista_telefonica_arquivo/telefones.txt'

print('Digite oque você desejar fazer!')
print('1 - Cadastrar')
print('2 - Listar')
print('3 - Consultar')
print('4 - Excluir ')
escolha = input('<<< ')

if escolha == '1':
    with open(nome_do_arquivo, 'a') as arquivo:
        nome = input('Digite o nome para cadastrar <<< ').upper()
        telefone = input('Digite o número para cadastrar <<< ')
        arquivo.write(nome + ' - ')
        arquivo.write(telefone + '\n')
        
elif escolha == '2':
    with open(nome_do_arquivo, 'r') as arquivo:
        for linha in arquivo.readlines():
            print(linha, end='')

elif escolha == '3':
    with open(nome_do_arquivo, 'r') as arquivo:
        nome_consulta = input('Digite o nome para consultar <<< ').upper()
        
        for linha in arquivo.readlines():
            if nome_consulta in linha:
                print(linha)

    
elif escolha == '4':
    with open(nome_do_arquivo, 'r+') as arquivo:
        nome_excluir = input('Digite o nome para excluir <<< ').upper()
        linhas = arquivo.readlines()
        arquivo.seek(0)
        for indice, linha in enumerate(linhas):
            if nome_excluir in linha:
                linhas.pop(indice)
                
        arquivo.writelines(linhas)
        arquivo.truncate()

else:
    print('Opção invalida')