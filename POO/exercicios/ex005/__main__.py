from rich import inspect
from classesex005 import Aluno, Professor, Funcionario


a1 = Aluno(nome="Matheus", idade=21, curso="TI", turma="Sala b2")
a1.FazerAniversario()
a1.FazerMatricula()
#inspect(a1)


p1 = Professor("Jose", 30, "Tec.Informatica", "Doutorado")
#inspect(p1)
p1.DarAula()


f1 = Funcionario("Ana", 20, "Assistente", "RH")
#inspect(f1)
f1.BaterPonto()