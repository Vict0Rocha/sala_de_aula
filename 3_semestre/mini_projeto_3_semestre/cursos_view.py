class CursoView:
    @staticmethod
    def exibir_cursos(cursos):
        if not cursos:
            print("Nenhum curso cadastrado.")
        else:
            for curso in cursos:
                print(curso)

    @staticmethod
    def exibir_mensagem(mensagem):
        print(mensagem)

    @staticmethod
    def capturar_dados_curso():
        codigo = input("Digite o código do curso: ")
        nome = input("Digite o nome do curso: ")
        duracao = input("Digite a duração do curso (em meses): ")
        nome_professor = input("Digite o nome do professor: ")
        especialidade_professor = input(
            "Digite a especialidade do professor: ")
        return codigo, nome, duracao, nome_professor, especialidade_professor

    @staticmethod
    def capturar_codigo():
        return input("Digite o código do curso: ")


class ProfessorView:
    @staticmethod
    def exibir_professor(professor):
        print(professor)

    @staticmethod
    def capturar_dados_professor():
        nome = input("Digite o nome do professor: ")
        especialidade = input("Digite a especialidade do professor: ")
        return nome, especialidade
