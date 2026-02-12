from rich import print
from rich.panel import Panel
from rich.traceback import install
install()

class gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []
    
    def add_favoritos(self, jogo):
        self.jogos.append(jogo)

    def ficha(self):
        self.jogos.sort()
        jogosFormatados = "\n".join(f"- {jogo}" for jogo in self.jogos)

        caixa = Panel(f"Nome Real: {self.nome}\nJogos favoritos:\n{jogosFormatados}", title=f"Jogador <{self.nick}>", width=35)
        print(caixa)
        
    

j1 = gamer(nome='Matheus', nick='theus')

j1.add_favoritos('fortnite')
j1.add_favoritos('call')
j1.ficha()

j2 = gamer(nome='Diego', nick='careca')

j2.add_favoritos('Gta')
j2.add_favoritos('Roblox')
j2.add_favoritos('Clash')
j2.ficha()