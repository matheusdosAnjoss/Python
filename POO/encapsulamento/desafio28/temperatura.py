class Termostato():
    def __init__(self, temperatura_inicial: float = 24.0):
        self.MIN_TEMP = 16.0
        self.MAX_TEMP = 30.0

    # Inicializa a temperatura validando o valor inicial
        if self.MIN_TEMP <= temperatura_inicial <= self.MAX_TEMP:
            self.__temperatura = temperatura_inicial
        else:
            self.__temperatura = 24.0


    @property
    def temperatura(self) -> float:
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, nova_temp: float):
        if self.MIN_TEMP <= nova_temp <= self.MAX_TEMP:
            self.__temperatura = nova_temp
        else:
            print(f'ERRO: A temperatura deve estar entre {self.MIN_TEMP}ºC e {self.MAX_TEMP}ºC')


    def aumentar(self):
        self.temperatura += 0.5
        print(f'Após aumentar: {self.temperatura}ºC')

    def diminiur(self):
        self.temperatura -= 0.5
        print(f'Após diminuir: {self.temperatura}ºC')

    def __str__(self):
        return f"Termostato ajustado em: {self.__temperatura}ºC"


# 1. Criando o termostato (inicia em 20°C por padrão)
t = Termostato()
print(t)
# inspect(t, private=True, methods=True)

# 2. Aumentando a temperatura usando o método de incremento
t.aumentar()

# 3. Tentando definir um valor diretamente via propriedade (Setter)
t.temperatura = 29.5
print(f"Ajuste manual: {t.temperatura}°C")

# 4. Tentando estourar o limite máximo (30°C)
t.aumentar()
t.diminiur()

# 5. Tentando forçar um valor abaixo do mínimo (16°C)
t.temperatura = 12