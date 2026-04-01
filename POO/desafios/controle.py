from rich import print
from rich.panel import Panel

"""
Módulo de controle remoto simulado para uma TV simples usando Rich para UI.
Contém a classe ControleRemoto e um loop interativo para testar comandos.
"""

class ControleRemoto:
    """
    Classe que representa um controle remoto para TV.
    
    Atributos de classe:
        canal_min (int): Canal mínimo disponível (padrão 1).
        canal_max (int): Canal máximo disponível (padrão 6).
        volume_min (int): Volume mínimo (padrão 1).
        volume_max (int): Volume máximo (padrão 5).
    """
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
                self.canal_atual += 1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == self.canal_min:
                self.canal_atual = self.canal_max
            else:
                self.canal_atual -= 1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual != self.volume_max:
                self.volume_atual += 1

    def volume_menos(self):
        if self.ligado:
            if self.volume_atual != self.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):

        conteudo = ''
        if self.ligado == False:
            conteudo = ('[red]A tv esta desligada')
        else:
            conteudo = f"CANAL = "

            for canal in range(self.canal_min, self.canal_max +1 ):
                if canal == self.canal_atual:       
                    conteudo += f"[yellow on yellow]  {canal} [/] "
                else: 
                    conteudo += f" {canal} "

            conteudo += f"\nVOLUME = "
            
            for volume in range(self.volume_min, self.volume_max +1):
                if volume <= self.volume_atual:
                    conteudo += "[black on yellow]  [/]"
                else: 
                    conteudo += "[black on white]  [/]"

        tv = Panel(conteudo, title="[ TV ]", width=32, padding=1)
        print(tv)

c = ControleRemoto()

while True:
    c.mostrar_tv()
    comando = str(input(f'< CH{c.canal_atual}>  - VOL{c.volume_atual} + : '))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '>':
            c.canal_mais()
        case '<':
            c.canal_menos()
        case '-':
            c.volume_menos()
        case '+':
            c.volume_mais()