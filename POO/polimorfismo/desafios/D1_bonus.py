from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome="", salario=0):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        if novo_salario > self.__salario:
            self.__salario = novo_salario
            return self.__salario
        else:
            print("Erro: O novo salário deve ser maior que o atual!")

    @abstractmethod
    def calcular_bonus():
        pass


class Gerente(Funcionario): 
    def calcular_bonus(self):
        return self.salario * 0.15

    def __str__(self):
        bonus = self.salario * 0.15
        return f"{self.nome} ganha R${self.salario:.2f} e por ser gerente o bonus será de R${bonus:.2f}"

class Designer(Funcionario): 
    def calcular_bonus(self):
        return self.salario * 0.08
    
    def __str__(self):
        bonus = self.salario * 0.08
        return f"{self.nome} ganha R${self.salario:.2f} e por ser desiner o bonus será de R${bonus:.2f}"

class Desenvolvedor(Funcionario): 
    def calcular_bonus(self):
        return self.salario * 0.10
   
    def __str__(self):
        bonus = self.salario * 0.10
        return f"{self.nome} ganha R${self.salario:.2f} e por ser desenvolvedor o bonus será de R${bonus:.2f}"

f = Gerente('ana', 2000)
f.salario = 1000
print(f)