from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min: int = 1
    canal_max: int = 6
    volume_min: int = 1
    volume_max: int = 5

    
    def __init__(self, canal = 1, volume = 2):
        self.canal_atual: int = canal
        self.volume_atual: int = volume
        self.ligado: bool = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == self.canal_max:
                self.canal_atual = self.canal_min
            else:
                self.canal_atual += 1 #15min esta dando erro

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        pass

    def volume_menos(self):
        pass

    def mostrar_tv(self):

        conteudo = ''
        if self.ligado == False:
            conteudo = ('[red]A tv esta desligada')
        else:
            conteudo = f"CANAL = "

            for canal in range(self.canal_min, self.canal_max ):
                if canal == self.canal_atual:       
                    conteudo += f"[yellow on yellow]  {canal} [/] "
                else: 
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME = "
            
            for volume in range(self.volume_min, self.volume_max +1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on yellow]   [/]"
                else: 
                    conteudo += f"[black on white]   [/] "

        tv = Panel(conteudo, title="[ TV ]", width=32)
        print(tv)

c = ControleRemoto(canal=1, volume=3)
c.liga_desliga()
c.canal_menos()
c.mostrar_tv()