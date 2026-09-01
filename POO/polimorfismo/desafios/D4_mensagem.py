from rich.console import Console
from rich.panel import Panel

console = Console()

class Mensagem:
    def __init__(self, mensagem, tipo, icone):
        self._mensagem = mensagem
        self._tipo = tipo
        self._icone = icone

    def mostrar(self):
        conteudo = f"{self._icone}  {self._mensagem}"
        painel = Panel(
            conteudo,
            title=f"[bold]{self._tipo}[/bold]",
            expand=False
        )
        console.print(painel)

class Error(Mensagem):
    def __init__(self, mensagem):
        super().__init__(
            mensagem = mensagem,
            tipo="[bold red]ERROR[/bold red]",
            icone="❌"
        )


class Aviso(Mensagem):
    def __init__(self, mensagem):
        super().__init__(
            mensagem = mensagem,
            tipo="[bold yellow]AVISO[/bold yellow]",
            icone="⚠️"
        )

msg_generica = Mensagem(
        mensagem="Operação realizada com sucesso!",
        tipo="[bold green]INFO[/bold green]",
        icone="ℹ️"
    )
msg_error = Error('Não foi possível conectar ao banco de dados.')
msg_aviso = Aviso("Sua sessão expira em 5 minutos.")

msg_generica.mostrar()
msg_error.mostrar()
msg_aviso.mostrar()