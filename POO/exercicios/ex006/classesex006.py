from abc import ABC, abstractmethod #classe abstrato

# --- CLASSES ABSTRATAS (O CONTRATO) ---
# 1. É a "mãe mandona": ela define as regras, mas não coloca a mão na massa.
# 2. Proibido criar objetos: você não cria um "Animal", cria um "Cão". Se tentar, o Python trava.
# 3. @abstractmethod: é o "voto de compromisso". A filha que herdar TEM que escrever esse método.
# 4. Organização total: garante que suas classes diferentes falem a mesma língua (mesmos métodos).

class Pessoa(ABC):  #Super Class
    def __init__(self, nome="", idade= 0):
        self.nome = nome
        self.idade = idade

    def FazerAniversario(self): #METODO
        self.idade += 1

    @abstractmethod #Metodo abstrato
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def FazerMatricula(self): #METODO
        print(f"{self.nome} acabou de fazer matricula")

    def estudar(self):
        print(f'O Aluno {self.nome} estudando {self.curso} na turma: {self.turma}')
    


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def DarAula(self): #METODO
        print(f"Prof.{self.nome} Especializado em {self.especialidade} com nivel de {self.nivel}")
    
    def estudar(self):
        print(f'O professor {self.nome} estudar {self.especialidade}')



class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def BaterPonto(self): #METODO
        print(f'{self.nome} acabou de bater o ponto!')

    def estudar(self):
        print(f'A funcionario {self.nome} estudar {self.setor}')