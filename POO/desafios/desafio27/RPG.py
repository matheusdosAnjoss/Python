from abc import ABC, abstractmethod
from random import randint
from rich import print

# Esta é a "Forma Base" para todos os personagens
class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida  # Guardamos o total de vida
        self.hp_atual = vida # No começo, a vida atual é igual ao total

    # Ação de bater em alguém
    def atacar(self, alvo, forca):  
        # Sorteia um número de 1 a 20 (como um dado de RPG) para decidir o dano
        dano = forca * randint(1, 20) / 20

        # Escolhe um golpe aleatório da lista de golpes do personagem
        golpe_escolhido = self.golpes[randint(0, len(self.golpes) - 1)]
        
        print(f'{self.nome} atacou {alvo.nome} com {golpe_escolhido} (Força: {forca})')

        # Avisa o alvo que ele foi atingido
        alvo.receber_dano(dano)

    # Ação de sentir o golpe
    def receber_dano(self, dano):
        self.hp_atual -= dano # Diminui os pontos de vida
        print(f'{self.nome} recebeu {dano:.1f} de dano!') # Mostra o dano com 1 casa decimal
        
    # Verifica se o herói ainda está de pé
    def vivo(self):
        if self.hp_atual > 0:
            print(f'[vermelho]{self.nome}[/] está agora com {self.hp_atual:.1f} de vida')
            return True
        else:
            print(f'{self.nome} foi derrotado!')
            return False

    # Todo personagem é OBRIGADO a saber curar, mas cada um faz do seu jeito
    @abstractmethod
    def curar(self):
        pass

# Criando o Guerreiro que "puxa" as coisas do Personagem
class Guerreiro(Personagem):
    golpes = ['Golpe Flamejante', 'Impactor explosivo']

    def curar(self):
        if self.hp_atual > 0:
            cura = randint(10, 50) # Sorteia quanto de vida vai recuperar
            print(f'O {self.nome} fez uma atadura e recuperou {cura} pontos de vida')
            self.hp_atual += cura
        else:
            print(f'{self.nome} não pode se curar porque já caiu!')

# Criando o Mago que também "puxa" as coisas do Personagem
class Mago(Personagem):
    golpes = ['Lança de fogo', 'Lança de Gelo']

    def curar(self):
        if self.hp_atual > 0:
            cura = randint(15, 60) # Magia costuma curar um pouco mais!
            print(f'O {self.nome} lançou uma magia de cura e recuperou {cura} pontos de vida')
            self.hp_atual += cura
        else:
            print(f'{self.nome} está sem mana e sem vida para conjurar!')



# p1 = Guerreiro('Kratos', 3000)
# p2 = Mago('Merlin', 3000)

# p1.atacar(p2, 1000)
# p2.atacar(p1, 2000)
def main():

    p1 = Guerreiro('Kratos',3000)
    p2 = Mago('Merlin',3000)
    
    while True:
        if p1.vivo():
            p1.atacar(p2,1000)
            p2.curar()
        else:
            print(f'{p1.nome} foi derrotado.')
            break
        
        if p2.vivo():
            p2.atacar(p1,1000)
            p1.curar()
        else:
            print(f'{p2.nome} foi derrotado.')
            break

if __name__ == '__main__':
    main()