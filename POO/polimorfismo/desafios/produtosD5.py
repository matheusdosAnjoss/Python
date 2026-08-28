class Produto:
    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco


class Carrinho:
    def __init__(self):
        self.produtos = []

    @property
    def total(self) -> float:
        return sum(p.preco for p in self.produtos)

    def __add__(self, produto: Produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)
            return self  # Retorna o próprio carrinho para permitir encadeamento
        raise TypeError("Apenas objetos da classe 'Produto' podem ser adicionados.")

    def __str__(self):
        return f"Produtos no carrinho:\n {[p.nome for p in carrinho.produtos]}\n Total: R$ {carrinho.total:.2f}"

p1 = Produto('Mouse', 150)
p2 = Produto('Monitor', 600)
p3 = Produto('Teclado', 200)
p4 = Produto('Fone', 100)

carrinho = Carrinho()

carrinho + p1 + p2 + p3 + p4

print(carrinho)

