from rich import inspect
class Retangulo:
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
        self._area = base * altura

    # @property para a Base
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, novo_valor):
        if novo_valor > 0:
            self._base = novo_valor
            self._atualizar_area()
        else:
            print('A base deve ser maior que zero!')

    # @property para a Altura
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, novo_valor):
        if novo_valor > 0:
            self._altura = novo_valor
            self._atualizar_area()
        else:
            print('A altura deve ser maior que zero!')

    # @property para as Medidas (retorna base e altura juntas)
    @property
    def medidas(self):
        return self._base, self._altura
    
    @property
    def area(self):
        return self._area

    def _atualizar_area(self):
        self._area = self._base * self._altura

r =  Retangulo(5, 3)
# inspect(r, private=True, methods=True)
print(f'Base: {r.base}')
print(f'Altura: {r.altura}')
print(r.medidas)
print(f'Area calculada = {r.area}')