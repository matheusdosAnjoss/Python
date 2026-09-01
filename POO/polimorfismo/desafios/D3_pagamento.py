from abc import ABC, abstractmethod


class Pagamento(ABC):
    def __init__(self, valor:float):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @abstractmethod
    def pagar(self):
        pass

class Boleto(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIMADO de R${self.valor:.2f} via Boleto!')

class Credito(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIMADO de R${self.valor:.2f} via Credito!')

class Pix(Pagamento):
    def pagar(self):
        print(f'Pagamento CONFIMADO de R${self.valor:.2f} via Pix!')


# Criando uma lista de pagamentos (Polimorfismo em ação)
pagamentos = [
    Boleto(150.00),
    Pix(89.90),
    Credito(1200.50)
]

# Processando cada pagamento
for p in pagamentos:
    p.pagar()