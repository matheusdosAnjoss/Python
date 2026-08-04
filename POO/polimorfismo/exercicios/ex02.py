from abc import ABC

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e esta emitindo um som')

class Gato(Animal):
    def fazer_som(self):
        print(f'{self.nome} acbou de dizer MIAU!')


class Cachorro(Animal):
    def fazer_som(self):
        print(f'{self.nome} acbou de dizer AU! AU! AU!')

class Spitz(Cachorro):
    def fazer_som(self):
        print(f'{self.nome} acbou de dizer au! au! au! au! au!')

class PitBul(Cachorro):
    def fazer_som(self):
        print(f'{self.nome} acbou de dizer RUF! RUF! RUF!')


class Pato(Animal):
    def fazer_som(self):
        print(f'{self.nome} acbou de dizer QUAC! QUAC!')

class Galinha(Animal):
    def fazer_som(self):
        print(f'{self.nome} acbou de dizer PO! PO! PO!')


a = Cachorro('Molly')
a.fazer_som()

b = Gato('Marir')
b.fazer_som()

c = Pato('Donant')
c.fazer_som()

d = Galinha('jojo')
d.fazer_som()

e = Spitz('lulu')
e.fazer_som()

f = PitBul('trovão')
f.fazer_som()