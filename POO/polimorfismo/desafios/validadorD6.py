from abc import ABC, abstractmethod
import re

class Validador(ABC):
    @abstractmethod
    def validar(self, texto: str) -> bool:
        pass

class Usuario(Validador):
    def validar(self, texto:str)  -> bool:
        padrao = r'^[a-z0-9_]{5,20}$'
        return bool(re.match(padrao, texto))

class Senha(Validador):
    def validar(self, texto:str)  -> bool:
        padrao = r'^(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8,}$'
        return bool(re.match(padrao, texto))

class Email(Validador):
    def validar(self, texto:str)  -> bool:
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, texto))

# 3. Função Auxiliar que executa o polimorfismo
def validar_dado(validador: Validador, valor: str):
    eh_valido = validador.validar(valor)
    status = "SIM" if eh_valido else "NÃO"
    print(f"Valor: {valor} é válido? {status}")

validar_dado((Usuario()), valor='gus1234')
validar_dado((Email()), valor='gus1234@gmail.com')
validar_dado((Senha()), valor='Gus12345@')
