from rich import print

class livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1

        print(f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas} paginas no total. Você agora está na página {self.pagina_atual}")

    def avançar_paginas(self, n):
        cont = 0
        while cont < n and self.pagina_atual < self.paginas:
            print(f'pag {self.pagina_atual+1}', end= ' > ')
            self.pagina_atual += 1
            cont += 1

        print(f'[blue]Você avançou {n} paginas e agora esta na [red]pagina {self.pagina_atual}')


l1 = livro(titulo='10 coisas que aprendi', paginas=20)
l1.avançar_paginas(6)
l1.avançar_paginas(5)
l1.avançar_paginas(10)
                    #11:30