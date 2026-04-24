from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print
class Funcionario(ABC):
    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.sal_min = 1612
        self.inss = 0.075

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal():
        pass

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        bruto_calc = valor_hora * horas_trab
        super().__init__(nome, bruto_calc)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def calc_sal(self):
        desconto = self.sal_bruto * self.inss
        liquido = self.sal_bruto - desconto
        salario_minimo = liquido / self.sal_min
        nome_classe = type(self).__name__
        # return f'{self.nome} recebe R${liquido}'
    
        caixa = Panel(f"O salario de [blue]{self.nome}[/] ([purple]{nome_classe}[/]) é de [green]R${liquido:.2f}[/] e corresponde a [red]{salario_minimo:.1f} salarios minimos." ,title='Analise de Salario', width=50)
        print(caixa)
    

class FuncionarioMensalista(Funcionario):
    def calc_sal(self):
        desconto = self.sal_bruto * self.inss
        liquido = self.sal_bruto - desconto
        salario_minimo = liquido / self.sal_min
        nome_classe = type(self).__name__
        
        caixa = Panel(f"O salario de [blue]{self.nome}[/] ([purple]{nome_classe}[/]) é de [green]R${liquido:.2f}[/] e corresponde a [red]{salario_minimo:.1f} salarios minimos." ,title='Analise de Salario', width=50)
        print(caixa)
    


f1 = FuncionarioHorista(nome='paulo', valor_hora=12, horas_trab=200)
f1.calc_sal()

f2 = FuncionarioMensalista(nome='Ana', sal_bruto=9500)
f2.calc_sal()
