class Carteira:

    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Voce não tem autorização para alterar o saldo desse jeito!")

    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

c1 = Carteira()
c2 = Carteira()
print(c1 == c2)
print(c1.saldo)
# c1.saldo = 100