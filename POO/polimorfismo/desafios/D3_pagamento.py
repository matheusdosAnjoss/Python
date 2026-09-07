from abc import ABC, abstractmethod
import locale


class Pagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        if valor > 0:
            self.__valor = valor
        else:
            raise ValueError("O pagamento só pode ser efetuado para valores positivos.")

    @property
    def fvalor(self):
        try:
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        except locale.Error:
            try:
                locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
            except locale.Error:
                locale.setlocale(locale.LC_ALL, '')
        return locale.currency(self.__valor, grouping=True)

    @abstractmethod
    def pagar(self):
        pass


class Boleto(Pagamento):
    def pagar(self):
        return f'Pagamento CONFIMADO de {self.fvalor} via Boleto!'


class Credito(Pagamento):
    def pagar(self):
        return f'Pagamento CONFIMADO de {self.fvalor} via Credito!'


class Pix(Pagamento):
    def pagar(self):
        return f'Pagamento CONFIMADO de {self.fvalor} via Pix!'


def finalizarCompras(pagamento: Pagamento):
    print(pagamento.pagar())


finalizarCompras(Boleto(500.53))
finalizarCompras(Credito(5000.90))

# Criando uma lista de pagamentos (Polimorfismo em ação)
# pagamentos = [
#     Boleto(150.00),
#     Pix(89.90),
#     Credito(1200.50)
# ]
#
# # Processando cada pagamento
# for p in pagamentos:
#     print(p.pagar())