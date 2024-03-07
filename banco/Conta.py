class Conta:
    def __init__(self, titular, numero):
        self._saldo = 0.0
        self._numero = numero
        self._titular = titular

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if saldo < 0:
                print("O saldo não pode ser negativo")
            else:
                self._saldo = saldo

    def saque(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

    def depositar(self, valor):
        self._saldo += valor

    def extrato(self):
        print(f"Cliente: {self._titular} Saldo atual: {self._saldo}")
