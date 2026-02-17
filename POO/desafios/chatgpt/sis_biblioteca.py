from rich import print

def linha(tam=25):
    print('='*tam)

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        
    
class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    def adicionar_livro(self, livro):
        self.lista_livros.append(livro)

    def lista_de_livro(self):
        if not self.lista_livros:
            print('nenhum livro cadastrado')
            return
        
        linha()
        for livro in self.lista_livros:
            print(f'Titulo: {livro.titulo}')
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano}")
            linha()

    def buscar_livro(self, titulo):
        for livro in self.lista_livros:
            if livro.tittulo.lower() == titulo.lower():
                return livro
        return None
    

biblioteca = Biblioteca()

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        linha()
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        ano = input('Ano: ')

        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

        print('[green]Livro Cadastrado')
        linha()
    elif opcao == '2':
        biblioteca.lista_de_livro()
    elif opcao == '3':
        break
