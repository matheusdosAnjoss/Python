class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

blibioteca = list()
while True:
    print('1 - Adicionar livro')
    print('2 - Listar livro')
    print('3 - Sair')

    escolha = input('Escolhar: ')

    if escolha == '1':
        titulo = str(input('Titulo do livro: '))
        autor = str(input('Autor do livro: '))
        livro = Livro(titulo, autor)
        blibioteca.append(livro)
        print('Livro adicionado!')

    elif escolha == '2':
        print('='*20)
        for i, livro in enumerate(blibioteca):
            print(f'{i+1} - {livro.titulo} | {livro.autor}')
        print('='*20)
        
    elif escolha == '3':
        break
    else:
        print('='*20)
        print("ERRO tente novamente!")
        print('='*20)

print(blibioteca)