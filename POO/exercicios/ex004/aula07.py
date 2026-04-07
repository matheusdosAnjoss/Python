from rich import inspect

class Pessoa:  #Super Class
    def __init__(self, nome="", idade= 0):
        self.nome = nome
        self.idade = idade

    def FazerAniversario(self): #METODO
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def FazerMatricula(self): #METODO
        print(f"{self.nome} acabou de fazer matricula")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def DarAula(self): #METODO
        print(f"Prof.{self.nome} Especializado em {self.especialidade} com nivel de {self.nivel}")
        

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def BaterPonto(self): #METODO
        print(f'{self.nome} acabou de bater o ponto!')



a1 = Aluno(nome="Matheus", idade=21, curso="TI", turma="Sala b2")
a1.FazerAniversario()
a1.FazerMatricula()
#inspect(a1)


p1 = Professor("Jose", 30, "Back-end", "Doutorado")
#inspect(p1)
p1.DarAula()


f1 = Funcionario("Ana", 20, "Assistente", "RH")
#inspect(f1)
f1.BaterPonto()