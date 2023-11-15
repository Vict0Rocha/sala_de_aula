print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')
print('')

# lista_nome = []
# lista_telefone = []


print('Digite oque você desejar fazer!')
print('1 - Cadastrar')
print('2 - Listar')
print('3 - Consultar')
print('4 - Excluir ')
escolha = input('<<< ')

if escolha == '1':
    with open('lista_telefonica_arquivo/telefones.txt', 'a') as arquivo:
        nome = input('Digite o nome para cadastrar <<< ')
        telefone = input('Digite o nome para cadastrar <<< ')
        arquivo.write(nome + ' - ')
        arquivo.write(telefone + '\n')
        
elif escolha == '2':
    with open('lista_telefonica_arquivo/telefones.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha, end='')

elif escolha == '3':
    with open('lista_telefonica_arquivo/telefones.txt', 'r') as arquivo:
        nome_consulta = input('Digite o nome para consultar <<< ')
        nomes = set()
        for linha in arquivo.readline():
            nomes.add(linha)

        print(nomes)
elif escolha == '4':
    with open('lista_telefonica_arquivo/telefones.txt', 'r') as arquivo:
        pass

else:
    print('Opção invalida')