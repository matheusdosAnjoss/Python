from rich import print
from rich.table import Table

tabela = Table(title='Tabela de Preços')

tabela.add_column('Nome')
tabela.add_column('Preço')

tabela.add_row('[red]Bolo', 'R$10,99')
tabela.add_row()

print(tabela)