from cursos_controller import CursoController


def main():
    controller = CursoController()

    while True:
        print("\n--- Sistema de Gerenciamento de Cursos ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Editar")
        print("4. Excluir")
        print("5. Sair")
        opcao = input("Escolha uma opção <<< ")

        if opcao == '1':
            controller.cadastrar_curso()
        elif opcao == '2':
            controller.listar_cursos()
        elif opcao == '3':
            controller.editar_curso()
        elif opcao == '4':
            controller.excluir_curso()
        elif opcao == '5':
            print("Saindo do sistema.")
            break
        else:
            print("[ERRO] - Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
