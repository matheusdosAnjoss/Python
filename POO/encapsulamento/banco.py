from rich import inspect
class ContaBancaria:
    """
   Cria uma conta bancaria e permite fazer saques de depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.__saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual tem R${self.__saldo}')

    def exibirSaldo(self):
        return f"A conta {self.id} de {self.titular} tem R${self.__saldo:,.2f} de saldo"

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Deposito de R${valor:.2f} autorizado na conta {self.id}')
        else:
            print(f'Ei! Você não pode depositar um valor negativo: (R${valor})')

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')
            
        else:
            print(f'Saldo insuficiente ou valor inválido.')


c1 = ContaBancaria(id=112, nome="Gustavo", saldo=3000)
c1.deposito(500)
c1.deposito(-800)
c1.sacar(-500)
print(c1.exibirSaldo())

