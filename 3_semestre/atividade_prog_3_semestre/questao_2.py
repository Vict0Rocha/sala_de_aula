'''Questão 2
Implementação de uma classe conta corrente com atributos privados
'''


class ContaCorrente:
    def __init__(self, numero_conta: int, titular: str, senha: str,
                 saldo: float = 0):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def __verificar_senha(self, senha) -> bool:
        return self.__senha == senha

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Deposito concluído no valor de: R${valor:.2f}")
        else:
            print("Valor inválido para depósito")

    def sacar(self, valor, senha):
        if not self.__verificar_senha(senha):
            print("Senha incorreta.")
        else:
            if valor <= self.__saldo and valor > 0:
                self.__saldo -= valor
                print(f"Saque concluído no valor de: R${valor:.2f}")
            else:
                print("Valor para saque inválido.")

    def consultar_saldo(self, senha):
        if not self.__verificar_senha(senha):
            print("Senha incorreta.")
        else:
            print(f"O saldo da sua conta é: R${self.__saldo:.2f}")


if __name__ == "__main__":
    p = ContaCorrente(555, 'Victor', 'AB')
    p.depositar(50)
    p.sacar(20, "AB")
    p.consultar_saldo("AB")
    p.depositar(50)
    p.consultar_saldo("AB")
    p.sacar(10, "AB")
    p.depositar(100)
    p.consultar_saldo("AB")
