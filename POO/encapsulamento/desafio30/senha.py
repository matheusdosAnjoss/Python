import hashlib

class Credencial:
    def __init__(self, senha_inicial):
        self.__hash = ""
        self.senha = senha_inicial

    @property
    def senha(self):
        return '*******'
    @senha.setter
    def senha(self, nova_senha):
        self.__hash = hashlib.sha256(nova_senha.encode('utf8')).hexdigest()

    @property
    def hash_seguro(self):
        return self.__hash

    def validar(self, chave):
        chave_hash = hashlib.sha256(chave.encode('utf8')).hexdigest()

        return chave_hash == self.__hash
    
c = Credencial('python')
print(f'Hash Hexadecimal {c.hash_seguro}')
print(f'Senha armazenada: {c.senha}')

print(c.validar('python123'))