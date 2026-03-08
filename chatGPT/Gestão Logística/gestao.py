from modulos import funcoes as modulos
from rich import print
from rich.panel import Panel
from rich.traceback import install
install()
"""
Sistema de Gestão Logística

Este programa implementa um sistema simples de gerenciamento de operações
logísticas, permitindo o controle de encomendas e veículos de transporte.
O sistema funciona através de um menu interativo no terminal, possibilitando
ao usuário cadastrar, consultar e gerenciar entregas.

Funcionalidades do sistema:
    1. Cadastrar encomenda:
        Registra uma nova encomenda informando cliente, origem, destino,
        peso e valor do frete. Cada encomenda recebe um código único.

    2. Listar encomendas:
        Exibe todas as encomendas cadastradas no sistema com suas
        respectivas informações.

    3. Atualizar status:
        Permite alterar o status de uma encomenda para:
        - Em rota
        - Entregue

    4. Cadastrar veículo:
        Registra um novo veículo na frota informando placa, tipo e
        capacidade máxima de carga.

    5. Alocar encomenda em veículo:
        Associa uma encomenda pendente a um veículo disponível,
        verificando se a capacidade do veículo suporta o peso da carga.

    6. Relatório logístico:
        Apresenta um resumo geral do sistema, incluindo:
        - Total de encomendas
        - Encomendas pendentes
        - Encomendas em rota
        - Encomendas entregues
        - Faturamento total
        - Situação da frota de veículos

    7. Buscar encomenda:
        Permite localizar encomendas por código ou pelo nome do cliente.

    8. Encerrar sistema:
        Finaliza a execução do programa.

Estrutura do programa:
    - O arquivo principal (gestao.py) controla o fluxo do sistema.
    - As funções operacionais estão organizadas no módulo "modulos".
    - As informações são armazenadas em listas durante a execução.

Variáveis principais:
    lista_encomenda (list): Armazena os dados das encomendas cadastradas.
    lista_veiculos (list): Armazena os dados dos veículos cadastrados.

Tecnologias utilizadas:
    - Python
    - Biblioteca Rich (para melhoria visual no terminal)

Autor:
    Matheus Oliveira

Curso:
    Engenharia de Software
"""

                 #PROGRAMA PRINCINPAL
lista_encomenda = []
lista_veiculos = []

while True:
    opcao = modulos.menu()

    if opcao == 1:
        lista_encomenda.append(modulos.cadastrar_encomenda(lista_encomenda))
    elif opcao == 2:
        modulos.lista_encomendas(lista_encomenda)
    elif opcao == 3:
        modulos.atualizar_status(lista_encomenda)
    elif opcao == 4: 
        lista_veiculos.append(modulos.cadastrar_veiculo())
    elif opcao == 5:
        modulos.alocar_encomenda(lista_encomenda, lista_veiculos)
    elif opcao == 6:
        modulos.relatorio(lista_encomenda, lista_veiculos)
    elif opcao == 7:
        modulos.buscar_encomenda(lista_encomenda)
    elif opcao == 8:
        print(modulos.linha())
        print('[green]Sistema encerrado.')
        print('[green]Obrigado por utilizar o sistema de gestão Logistica!')
        print(modulos.linha())
        break
