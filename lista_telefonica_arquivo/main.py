print(18 * '-')
print(' LISTA TELEFONICA')
print(18 * '-')
print('')

lista = []

print('Digite oque você desejar fazer!')
print('Cadastrar - 1')
print('Consultar - 2')
escolha = input('<<< ')

# if escolha == 1:
with open('lista_telefonica.txt', 'a', encoding='utf-8') as x:
    var = input('')
    x.write(var)