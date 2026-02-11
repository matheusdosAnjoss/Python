from rich import inspect
class ContaBancaria:
    """
   Cria uma conta bancaria e permite fazer saques de depositos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual tem R${self.saldo}')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def deposito(self, valor):
        self.saldo += valor
        print(f'Deposito de R${valor:.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque negado de R${valor:.2f} na conta {self.id}: SALDO INSUFICIENTE')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')


c1 = ContaBancaria(id=112, nome="Gustavo", saldo=3000)
c1.deposito(800)
c1.sacar(5000)
print(c1)
inspect(c1)