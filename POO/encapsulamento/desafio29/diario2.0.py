class Diario:
    def __init__(self, senha_inicial='Cev@'):
        self.__segredos = []
        self.__senha = senha_inicial.strip()

    def escrever(self, msg):
        self.__segredos.append(msg)
        print('Mensagem escrita com sucesso!')

    def ler(self, senha = None):
        if senha != self.__senha:
            print('Senha invalida! você não pode ler meu diario!')
        else:
            print("\n=== 📖 SEUS SEGREDOS REVELADOS ===")
            for i, segredo in enumerate(self.__segredos, 1):
                print(f"Página {i}: {segredo}")
            print("==================================\n")
       
    @property
    def senha(self):
        raise PermissionError(f'Niguem tem permisão de ver a senha!')
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
        print('Senha alterada com sucesso!')


d = Diario()
d.escrever('Hello word')
d.senha = '1234'
d.ler('Cev@')
