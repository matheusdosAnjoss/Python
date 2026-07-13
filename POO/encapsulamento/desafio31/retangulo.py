from rich import inspect
class Retangulo:
    def __init__(self, base= 1, altura= 1):
        self._base = None
        self._altura = None
        self._area = None

        self.base = base
        self.altura = altura

    # @property para a Base
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError('A base deve ser um numero maior q zero')
        self._base = novo_valor
        self._atualizar_area()
        

    # @property para a Altura
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError('A altura deve ser um numero maior q zero')
        
        self._altura = novo_valor
        self._atualizar_area()
      

    # @property para as Medidas (retorna base e altura juntas)
    @property
    def medidas(self):
        return self._base, self._altura
    
    @property
    def area(self):
        return self._area

    def _atualizar_area(self):
        # Só calcula se ambos os valores já tiverem sido definidos
        if self._base is not None and self._altura is not None:
            self._area = self._base * self._altura

r =  Retangulo(5, 7)
# r.altura = 7
# inspect(r, private=True, methods=True)
print(f'Base: {r.base}')

print(f'Altura: {r.altura}')
print(r.medidas)
print(f'Area calculada = {r.area}')