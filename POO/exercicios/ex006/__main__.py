from rich import inspect
from classesex006 import Pessoa, Aluno, Professor, Funcionario


a1 = Aluno(nome="Matheus", idade=21, curso="TI", turma="Sala b2")
a1.FazerAniversario()
a1.FazerMatricula()
a1.estudar()

print()

p1 = Professor("Jose", 30, "Tec.Informatica", "Doutorado")
p1.DarAula()
p1.estudar()

print()

f1 = Funcionario("Ana", 20, "Assistente", "RH")
f1.BaterPonto()
f1.estudar()

# x = Pessoa("Matheus", 20)
# x.FazerAniversario()
# inspect(x, methods=True)