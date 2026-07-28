from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, nascimento: date):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def nascimento(self) -> date:
        return self._nascimento

    @nascimento.setter
    def nascimento(self, novo_nascimento: date):
        self._nascimento = novo_nascimento


    @property
    def idade(self) -> int:
        hoje = date.today()
        return hoje.year - self._nascimento.year - (
            (hoje.month, hoje.day) < (self._nascimento.month, self._nascimento.day)
        )

    
class Aluno(Pessoa):
    cursos_oficias = ['Python', 'SQL', 'Java', 'C++']

    def __init__(self, nome:str, nascimento:date, curso: str = None):
        super().__init__(nome, nascimento)
        self._curso = []

        if curso:
            self.add_curso(curso)

    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, novo_curso):
        if novo_curso in self.cursos_oficias:
            if novo_curso not in self._curso:
                self._curso.append(novo_curso)
        else:
            raise ValueError(f"curso ' {novo_curso} ' não está na lista")

    def add_curso(self, curso:str):
        self.curso = curso     

    @classmethod
    def registrar_curso(cls, curso:str):
        if curso not in cls.cursos_oficias:
            cls.cursos_oficias.append(curso)
        else:
            print(f'O curso {curso} já está na lista')
 

p = Aluno(nome='ana', nascimento=date(2004, 10, 27))
print(p.nome)
print(f"idade do aluno: {p.idade}")

p.nascimento = date(2003, 10, 27)
print(f"idade do aluno: {p.idade}")

p.registrar_curso('ADS')
p.curso = 'ADS'
print(f"Cursos matriculados: {p.curso}")

p.registrar_curso('ADS')
print(p.cursos_oficias)

