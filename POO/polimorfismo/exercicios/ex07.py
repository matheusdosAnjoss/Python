class Numero:
    def __init__(self, valor:int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor = self.valor * 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do numero"

class Texto:
    def __init__(self, txt:str = ""):
        self.texto = txt
    
    def dobrar(self):
        self.texto = self.texto + " " + self.texto

    def __str__(self):
            return f"Tenho o texto '{self.texto}' dentro do texto"


class Lista:
    def __init__(self, lst:list = []):
        self.valores = lst
    
    def dobrar(self):
        self.valores = self.valores + self.valores

    def __str__(self):
            return f"Tenho a lista {self.valores} dentro da lista"


class Papel:
    def __init__(self):
        self.dobrado = False
    
    def dobrar(self):
        self.dobrado = True

    def __str__(self):
        return f"O papel esta dobrado? {self.dobrado}"

class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa muito engraçada"


    #DUCK TYPING
def tenteDobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f'Encontrei problemas ao tentar dobrar {objeto.__class__.__name__}')

a = Numero(200)
b = Texto("Gafanhoto")
c = Lista([1,2,3])
d = Papel()
e = Casa()

tenteDobrar(a)
tenteDobrar(b)
tenteDobrar(c)
tenteDobrar(d)
tenteDobrar(e)

print(a)
print(b)
print(c)
print(d)
print(e)