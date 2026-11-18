
from crud import cadastro_em_massa, cadastro_pessoas, listar_pessoas, atualizar_pessoas, excluir_pessoas, buscar_pessoa_por_nome


if __package__:
    from .crud import criar_banco
else:
    from crud import criar_banco

def exibir_menu():
    print("\n" + "=" * 30)
    print("      SISTEMA DE CADASTRO")
    print("=" * 30)
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Atualizar pessoa")
    print("4 - Excluir pessoa")
    print("5 - Busca por nome")
    print("0 - Sair")
    print("=" * 30)

def main():
    # cadastro_em_massa()

    if not criar_banco():
        print("Algum problema aconteceu ao criar o banco")
        raise SystemExit  


    while True:
        exibir_menu()
        opcao = input('Escolha sua opção: ').strip()

        match opcao:
            case "1":
                print("\n-> Opção selecionada: Cadastrar pessoa")
                cadastro_pessoas()
            case "2":
                # Chame aqui sua função de listagem, ex: listar_pessoas()
                if not listar_pessoas():
                    print("ERRO Não foi possivel atualizar o cadastro")

                listar_pessoas()

            case "3":
                print("\n-> Opção selecionada: Atualizar pessoa")
                # Chame aqui sua função de atualização, ex: atualizar_pessoa()
            case "4":
                print("\n-> Opção selecionada: Excluir pessoa")
                # Chame aqui sua função de exclusão
            case "5":
                # Chame aqui sua função de busca
                if not listar_pessoas():
                    print("ERRO Não foi possivel buscar o nome dessa pessoa")
                
                buscar_pessoa_por_nome()
            case "0":
                print("\nSaindo do sistema... Até logo!")
                break
            case _:
                print("\n[ERRO] Opção inválida! Tente novamente.")

        input("Pressione ENTER para continuar...")

if __name__ == '__main__':
    main()