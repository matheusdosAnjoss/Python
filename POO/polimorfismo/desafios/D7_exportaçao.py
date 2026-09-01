import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from abc import ABC, abstractmethod

# --- 1. Interface Base do Exportador ---

class Exportador(ABC):
    @abstractmethod
    def exportar(self, objetos: list) -> str:
        pass

class Aluno:
    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


# --- 2. Classes de Exportação ---
class XML(Exportador):
    def exportar(self, objetos: list) -> str:
        raiz = ET.Element("dados")
        
        for item in objetos:
            nome_tag = item.__class__.__name__.lower()
            elem_item = ET.SubElement(raiz, nome_tag)
            
            # Pega todos os atributos do objeto dinamicamente
            for chave, valor in item.__dict__.items():
                filho = ET.SubElement(elem_item, chave)
                filho.text = str(valor)

        # Formata o XML com indentação
        xml_str = ET.tostring(raiz, encoding="utf-8").decode("utf-8")
        dom = minidom.parseString(xml_str)
        return dom.toprettyxml(indent="  ")

class JSON(Exportador):
   def exportar(self, objetos: list) -> str:
        # Converte cada objeto em dicionário usando seu __dict__
        lista_dicts = [item.__dict__ for item in objetos]
        return json.dumps(lista_dicts, indent=4, ensure_ascii=False)


# --- 4. Função Principal ---
def exportar_dados(exportador: Exportador, objetos: list):
    resultado = exportador.exportar(objetos)
    print(resultado)


p1 = [
     Aluno("Ana", "Eng.Sofware", "3"),
     Usuario("Maria", "maria@gmail.com"),
]
  

exportar_dados(XML(), p1)
exportar_dados(JSON(), p1)