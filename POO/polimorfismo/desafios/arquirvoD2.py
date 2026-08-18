from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome=str, extensao=str, tamanho=float):
        self.nome = nome
        self._extensao = extensao
        self.tamanho = tamanho

    @property
    def nome_completo(self):
        return f"{self.nome}-{self.tamanho}"

    @abstractmethod
    def abrir(self):
        pass

class Pdf(Arquivo):
    def abrir(self):
        print(f"Abrindo arquivo '{self.nome}.pdf' ({self.tamanho}MB) no Adobe Reader")


class Word(Arquivo):
    def abrir(self):
        print(f"Abrindo arquivo '{self.nome}.doc' ({self.tamanho}MB) no Microsoft Word")

a = Pdf('prova', tamanho='250.000')
b = Word('Trabalho', tamanho='550.000')

a.abrir()
b.abrir()