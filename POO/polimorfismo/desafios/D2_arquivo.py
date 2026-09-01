from abc import ABC, abstractmethod

class Arquivo(ABC):
    def __init__(self, nome='', ext='', tamanho:int = 0):
        self.nome = nome
        self._extensao = None
        self.tamanho = tamanho
        self.extensao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extensao(self):
        return self._extensao

    @extensao.setter
    def extensao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extensao = ext
        else:
            raise AttributeError('O arquivo não suporta o formato')

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extensao}' ({self.tamanho/1000000}MB)"

    

class Pdf(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, ext='pdf', tamanho=tamanho)

    def abrir(self):
        print(f"Abrindo arquivo {self.nome_completo} no Adobe Reader")


class Word(Arquivo):
    def __init__(self, nome:str, tamanho:int):
        super().__init__(nome, ext='doc', tamanho=tamanho)

    def abrir(self):
        print(f"Abrindo arquivo {self.nome_completo} no Microsoft Word")


def abrir_arquivo(arquivo: Arquivo): 
    arquivo.abrir()


a = Pdf('prova', tamanho=1250000)
b = Word('Trabalho', tamanho=1550000)

abrir_arquivo(a)
abrir_arquivo(b)