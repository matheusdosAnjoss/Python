from abc import ABC, abstractmethod
import re

# 1. Classe Abstrata Base
class Validador(ABC):
    """
    Classe abstrata (Interface) que serve de modelo para todos os validadores.
    Ela define o contrato obrigatório: qualquer classe filha DEVE implementar
    o método 'validar'.
    """
    @abstractmethod
    def validar(self, texto: str) -> bool:
        pass


# 2. Validadores Específicos (Subclasses)
class Usuario(Validador):
    """
    Validador específico para nomes de usuário.
    Garante que o texto tenha entre 5 e 20 caracteres e contenha
    apenas letras minúsculas, números e sublinhados (_).
    """
    def validar(self, texto: str) -> bool:
        padrao = r'^[a-z0-9_]{5,20}$'
        return bool(re.match(padrao, texto))


class Senha(Validador):
    """
    Validador específico para senhas fortes.
    Garante que a senha tenha no mínimo 8 caracteres, contendo pelo menos
    uma letra maiúscula e pelo menos um caractere especial/símbolo.
    """
    def validar(self, texto: str) -> bool:
        padrao = r'^(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{8,}$'
        return bool(re.match(padrao, texto))


class Email(Validador):
    """
    Validador específico para endereços de e-mail.
    Garante a estrutura padrão (usuario@dominio.tld), verificando a presença do @,
    pontos no domínio e um TLD final válido de pelo menos 2 letras (ex: .com, .br).
    """
    def validar(self, texto: str) -> bool:
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
