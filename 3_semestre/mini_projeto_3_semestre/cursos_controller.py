from cursos_model import Curso, Professor
from cursos_view import CursoView


class CursoController:
    def __init__(self):
        self.cursos = []

    def cadastrar_curso(self):
        codigo, nome, duracao, nome_professor, especialidade_professor = CursoView.capturar_dados_curso()
        professor = Professor(nome_professor, especialidade_professor)
        curso = Curso(codigo, nome, duracao, professor)
        self.cursos.append(curso)
        CursoView.exibir_mensagem("Curso cadastrado com sucesso!")

    def listar_cursos(self):
        CursoView.exibir_cursos(self.cursos)

    def editar_curso(self):
        codigo = CursoView.capturar_codigo()
        for curso in self.cursos:
            if curso.codigo == codigo:
                _, nome, duracao, nome_professor, especialidade_professor = CursoView.capturar_dados_curso()
                curso.nome = nome
                curso.duracao = duracao
                curso.professor = Professor(
                    nome_professor, especialidade_professor)
                CursoView.exibir_mensagem("Curso editado com sucesso!")
                return
        CursoView.exibir_mensagem("Curso não encontrado.")

    def excluir_curso(self):
        codigo = CursoView.capturar_codigo()
        for curso in self.cursos:
            if curso.codigo == codigo:
                self.cursos.remove(curso)
                CursoView.exibir_mensagem("Curso excluído com sucesso!")
                return
        CursoView.exibir_mensagem("Curso não encontrado.")
