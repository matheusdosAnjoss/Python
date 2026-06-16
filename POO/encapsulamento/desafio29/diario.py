class Diario:
    def __init__(self, senha_inicial):
        self.__segredos = []
        self.__senha = senha_inicial

    def escrever(self, msg):
        self.__segredos.append(msg)
        print('Nova pagina escrita com sucesso!')

    def ler(self, senha):
        if senha == self.__senha:
            if not self.__segredos:
                print('O diario está vazio.')
            else:
                print("\n=== 📖 SEUS SEGREDOS REVELADOS ===")
                for i, segredo in enumerate(self.__segredos, 1):
                    print(f"Página {i}: {segredo}")
                print("==================================\n")
        else:
            print("❌ Senha incorreta! O diário permanece trancado.")


d = Diario('python')

d.escrever('Hoje eu passei no desafio de POO com o termostato!')
d.escrever('Acho que esqueci de tirar a carne do congelador...')
d.ler('python')
