from rich import print

"""
Sistema de Biblioteca em Python (POO)

Este programa simula um sistema simples de biblioteca utilizando
Programação Orientada a Objetos (POO). Ele permite:

- Cadastrar livros com título, autor e ano
- Listar todos os livros cadastrados
- Exibir informações formatadas no terminal
- Utilizar uma classe de layout para separar visualmente o conteúdo

O sistema é executado em modo interativo via terminal e utiliza
a biblioteca Rich para melhorar a saída de texto.

Classes:
    Livro       -> Representa um livro da biblioteca
    Layout      -> Responsável pela formatação visual (linhas divisórias)
    Biblioteca  -> Gerencia os livros cadastrados

Autor: Matheus Oliveira
"""

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

class Layout:
    def __init__(self, tam=25, simb='='):
        self.tam = tam
        self.simb = simb
    
    def linha(self):
        return self.simb * self.tam
        
class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    def adicionar_livro(self, livro):
        self.lista_livros.append(livro)
    
    def lista_de_livro(self):
        if not self.lista_livros:
            print('nenhum livro cadastrado')
            return
        
        print(layout.linha())
        for livro in self.lista_livros:
            print(f'Titulo: {livro.titulo}')
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano}")
            print(layout.linha())

    def buscar_livro(self, titulo):
        for livro in self.lista_livros:
            if livro.tittulo.lower() == titulo.lower():
                return livro
        return None
    

biblioteca = Biblioteca()
layout = Layout()

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        
        print(layout.linha())
        titulo = input('Titulo: ')
        autor = input('Autor: ')
        ano = input('Ano: ')

        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

        print('[green]Livro Cadastrado')
        print(layout.linha())

    elif opcao == '2':
        biblioteca.lista_de_livro()

    elif opcao == '3':
        break
