class Tv:
    def __init__(self, formato, polegadas, cor, marca, modelo, saida, volts = 'bivolts', *entrada):
        self.formato = formato
        self.polegadas = polegadas
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.saida_imagem =  saida
        self.volts = volts
        self.entrada = entrada
        self.is_state = False

    def estado(self):
        lista_entradas = []
        lista_entradas =  self.entrada
        print(f'Polegadas: {self.polegadas}')
        print(f'Formato: {self.formato}')
        print(f'Cor: {self.cor}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Saida da Imagem: {self.saida_imagem}')
        print(f'Voltz: {self.volts}')
        print('Entradas: ', end='')
        print(*lista_entradas, sep=', ')
            
    def on_of(self):
        print('1 - Ligar')
        print('2 - Desligar')
        try:
            state = int(input('<<< '))
            if state == 1:
                self.is_state = True
            elif state == 2:
                self.is_state = False
            else:
                print('Opção invalida.')

            if self.is_state == True:
                print('Sua TV está ligada')
            else:
                print('Sua TV está desligada')

        except ValueError as erro: # Tratando o erro e atribuindo para uma variavel.
            print('[ERRO] -',erro.__class__.__name__) # Exibindo o nome do erro, o mesmo de sua classe.
            print('Por favor, escolha somente uma das opções, 1 ou 2.')
        except Exception as erro:
            print('[ERRO] - Problema não detectado pelo sistema. ', erro.__class__.__name__)

    def trocar_canal(self):
        print('Digite o número do canal que deseja acessar.')
        try:
            canal = int(input('<<< '))
            print('Você mudou de canal.')
            print('Você está no canal -', canal)
        except ValueError as erro:
            print('[ERRO] -', erro.__class__.__name__)
            print('Por favor, digite somente números inteiros.')
        except Exception as erro:
            print('[ERRO] - Problema não detectado pelo sistema. ', erro.__class__.__name__)

    def conectar_dispositivo(self):
        lista_de_dispositivos = []
        print(lista_de_dispositivos)

        print('Digite o nome do novo dispositivo')
        novo_dispositivo = input('<<< ')
        if not novo_dispositivo in lista_de_dispositivos:
            lista_de_dispositivos.append(novo_dispositivo)
            print('Novo dispositivo conectado.')
        else:
            print('O dispositivo já estava conectado.')
        return lista_de_dispositivos


tv = Tv('retangular', 24, 'preta', 'AOC', 2.2, '4H', '110', 'HDMI', 'VGA')

