class TarefaView:

    def pegar_input(self, prompt):
        return input(prompt)

    def lista_tarefas(self, tarefas):
        for tarefa in tarefas:
            print(tarefa)

    def mostrar_mensagem(self, mensagem):
        print(mensagem)
