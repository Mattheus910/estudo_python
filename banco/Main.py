

class Main:
    pass

print("testando codigo")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("João", "4002-8922")
conta = Conta(c1.get_nome(), 6565)

conta.depositar(500)
conta.saque(100)
conta.extrato()