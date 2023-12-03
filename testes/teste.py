class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogadores = ["X", "O"]
        self.jogador_atual = self.jogadores[0]

    def exibir_tabuleiro(self):
        print("\n    0 | 1 | 2")
        print(" ---------------")
        for i, linha in enumerate(self.tabuleiro):
            print(f"{i} | {' | '.join(linha)}")

    def fazer_jogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            return True
        return False

    def verificar_vitoria(self):
        for i in range(3):
            if all(self.tabuleiro[i][j] == self.jogador_atual for j in range(3)) or \
                    all(self.tabuleiro[j][i] == self.jogador_atual for j in range(3)):
                return True
        return all(self.tabuleiro[i][i] == self.jogador_atual for i in range(3)) or \
               all(self.tabuleiro[i][2 - i] == self.jogador_atual for i in range(3))

    def verificar_empate(self):
        return all(self.tabuleiro[i][j] != " " for i in range(3) for j in range(3))

    def trocar_jogador(self):
        self.jogador_atual = self.jogadores[1] if self.jogador_atual == self.jogadores[0] else self.jogadores[0]

    def jogar(self):
        while True:
            self.exibir_tabuleiro()
            try:
                linha = int(input(f"Jogador {self.jogador_atual}, escolha a linha (0, 1, 2): "))
                coluna = int(input(f"Jogador {self.jogador_atual}, escolha a coluna (0, 1, 2): "))

                if 0 <= linha < 3 and 0 <= coluna < 3:
                    if self.fazer_jogada(linha, coluna):
                        if self.verificar_vitoria():
                            self.exibir_tabuleiro()
                            print(f"Jogador {self.jogador_atual} venceu!")
                            break
                        elif self.verificar_empate():
                            self.exibir_tabuleiro()
                            print("O jogo empatou!")
                            break
                        else:
                            self.trocar_jogador()
                    else:
                        print("Essa posição já está ocupada. Escolha outra.")
                else:
                    print("Posição inválida. Escolha novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")


if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
