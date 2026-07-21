from rich import inspect
import hashlib
import pwinput

class ContaBancaria:
    def __init__(self, id, saldo:float, titular= None,  senha=None):

        self._id = id
        self._titular = titular
        self.__saldo = saldo

        if senha is None:
            # senha = pwinput.pwinput(prompt='Crie uma senha: ', mask='*')
            senha = self.pede_senha()
            
        self.__hash = hashlib.sha256(senha.encode
        ('utf8')).hexdigest()

        print(f'Conta Bancaria com ID {self._id} de {self._titular} criada com sucesso!')
        print(f'----SAlDO DA CONTA: R${self.__saldo:.2f}----')

    @property
    def nome(self):
        return self._titular
    
    @nome.setter
    def nome(self, novo_nome):
        print('Vou tentar mudar de nome!')
        chave = self.pede_senha()

        if self.validar_senha(chave):
            self._titular = novo_nome
            print(f'Conta Bancaria com ID {self._id} de {self._titular} criada com sucesso!')
    

    def validar_senha(self, chave):
        chave_hex = hashlib.sha256(chave.encode('utf8')).hexdigest()
        return chave_hex == self.__hash
    

    def pede_senha(self):
        # return str(pwinput.pwinput(prompt='Digite sua senha: ', mask='*')).strip()
        while True:
            senha = str(pwinput.pwinput(prompt='Digite sua senha: ', mask='*')).strip()
            if len(senha) >= 6:
                break
            else:
                print('Senha Incorreta!')

        return senha


    def depositar(self, valor):
        if valor >= 0:
            self.__saldo += valor
            print(f'Deposito de R${valor:.2f} realizado!')
        else:
            print('valor invalido!')


    def sacar(self, valor):
        print('--'*15)
        print('Digite a senha para Sacar!')
        print('--'*15)
        chave = self.pede_senha()

        if not self.validar_senha(chave):
            print("Senha incorreta")
            return
    
        if valor > self.__saldo:
            print('Saldo Insuficiente')
            return
    
        self.__saldo -= valor
        print(f'Saque de R${valor:.2f} Realizado! Saldo da conta: R${self.__saldo:.2f}')


c = ContaBancaria(2222, 1000, 'ana')
c.nome = 'maria'
# inspect(c, private=True, methods=True)
c.depositar(500)
c.sacar(1000)

