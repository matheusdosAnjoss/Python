import hashlib

class Credencial:
    def __init__(self, senha_inicial='python'):
        self.__hash = ""
        self.senha = senha_inicial

    @property
    def senha(self):
        return self.__hash
    @senha.setter
    def senha(self, nova_senha):
        self.__hash = hashlib.sha256(nova_senha.encode('utf-8')).hexdigest()

    @property
    def hash_seguro(self):
        return self.__hash

    def validar(self, chave):
        chave_hash = hashlib.sha256(chave.encode('utf-8')).hexdigest()
    
        if chave_hash == self.__hash:
            return 'Senha confere!'
        else:
            return "Senha não bate!"

    
c = Credencial()
c.senha = str(input('Digiite sua senha: '))
# print(f'Hash Hexadecimal {c.hash_seguro}')
print(f'Senha armazenada: {c.senha}')

print(c.validar('python123'))