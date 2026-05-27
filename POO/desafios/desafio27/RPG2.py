from abc import ABC, abstractmethod
from random import randint
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from rich.text import Text
import time  

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida  
        self.hp_atual = vida 

    def atacar(self, alvo, forca):  
        dano = forca * randint(1, 20) / 20
        golpe_escolhido = self.golpes[randint(0, len(self.golpes) - 1)]  # de o a 2 ou 1
         
        # Log de ataque estilizado
        print(f"\n[bold yellow]⚔️  {self.nome}[/] usou [bold cyan]{golpe_escolhido}[/] contra [bold magenta]{alvo.nome}[/]!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.hp_atual -= dano
        if self.hp_atual < 0:
            self.hp_atual = 0
        print(f"💥 [bold red]{self.nome}[/] sofreu [bold red]{dano:.1f}[/] de dano!")

    def vivo(self):
        if self.hp_atual > 0:
            return True
        else:
            return False

    @abstractmethod
    def curar(self):
        pass

    # Método auxiliar para gerar o "Card" visual do personagem
    def gerar_status(self, cor_borda):
        # Calcula a porcentagem de vida para mudar a cor da barra de HP
        pct_vida = self.hp_atual / self.vida
        if pct_vida > 0.5:
            cor_hp = "green"
        elif pct_vida > 0.2:
            cor_hp = "yellow"
        else:
            cor_hp = "red"

        texto = f"[bold]HP:[/b] [{cor_hp}]{self.hp_atual:.1f}[/]/[green]{self.vida}[/]\n"
        # Cria uma barrinha de progresso visual simples
        barrinha = "🟩" * int(pct_vida * 10) + "⬛" * (10 - int(pct_vida * 10))
        texto += f"Status: {barrinha}"
        
        return Panel(texto, title=f"[bold]{self.nome}[/]", border_style=cor_borda, expand=True)


class Guerreiro(Personagem):
    golpes = ['Golpe Flamejante', 'Impactor Explosivo']

    def curar(self):
        if self.hp_atual > 0:
            cura = randint(10, 50)
            self.hp_atual += cura
            if self.hp_atual > self.vida: # Impede de curar acima do máximo
                self.hp_atual = self.vida
            print(f"🩹 [bold green]{self.nome}[/] aplicou ataduras e recuperou [green]+{cura}[/] de HP!")
        else:
            print(f"💀 {self.nome} não pode se curar porque já caiu!")


class Mago(Personagem):
    golpes = ['Lança de Fogo', 'Lança de Gelo']

    def curar(self):
        if self.hp_atual > 0:
            cura = randint(15, 60)
            self.hp_atual += cura
            if self.hp_atual > self.vida:
                self.hp_atual = self.vida
            print(f"✨ [bold green]{self.nome}[/] conjurou magia de cura e recuperou [green]+{cura}[/] de HP!")
        else:
            print(f"💀 {self.nome} está sem mana e sem vida para conjurar!")


def exibir_painel_combate(p1, p2):
    # Organiza os dois personagens lado a lado em colunas bonitas
    card_p1 = p1.gerar_status("blue")
    card_p2 = p2.gerar_status("magenta")
    print("\n" + "="*50)
    print(Columns([card_p1, card_p2]))
    print("="*50)



def main():
    p1 = Guerreiro('Kratos 🛡️', 2000)
    p2 = Mago('Merlin 🔮', 2000)
    
    rodada = 1
    

    print(Panel.fit("⚔️  [bold yellow]A BATALHA ÉPICA COMEÇOU![/] ⚔️", border_style="bold red"))
    
    while True:
        print(f"\n[bold white on blue]  RODADA {rodada}  [/]")
        exibir_painel_combate(p1, p2)
        time.sleep(1) # Pausa dramática de 1 segundo
        
        # Turno do Personagem 1
        if p1.vivo():
            p1.atacar(p2, 1000)
            if p2.vivo():
                p2.curar()
        else:
            print(Panel(f"🏆 [bold yellow]{p2.nome}[/] VENCEU A BATALHA!", border_style="yellow"))
            break
            
        # Turno do Personagem 2
        if p2.vivo():
            p2.atacar(p1, 1000)
            if p1.vivo():
                p1.curar()
        else:
            print(Panel(f"🏆 [bold yellow]{p1.nome}[/] VENCEU A BATALHA!", border_style="yellow"))
            break
            
        rodada += 1

if __name__ == '__main__':
    main()