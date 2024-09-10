from datetime import datetime
from model.tarefas_model import TarefaModel
from view.tarefas_view import TarefaView

class TarefaController:
    def __init__(self, session, view) -> None:
        self.session = session
        self.view = view

    def adicionar_tarefa(self):
        descricao = self.view.pegar_input('Descrição da tarefa: ')
        data_str = self.view.pegar_input('Data da tarefa (AAAA-MM-DD): ')
        prioridade = self.view.pegar_input('Prioridade da tarefa (alta, media, baixa): ')
        data = datetime.strptime(data_str, "%Y-%m-%d")

        nova_tarefa = TarefaModel(descricao=descricao, data=data, prioridade=prioridade)
        self.session.add(nova_tarefa)
        self.session.commit()
        self.view.mostrar_mensagem('A tarefa foi salva com sucesso!')

    def listar_tarefas(self):
        tarefas = self.session.query(TarefaModel).all()
        if tarefas:
            for tarefa in tarefas:
                mensagem = (
                    f"ID: {tarefa.id}, "
                    f"Descrição: {tarefa.descricao}, "
                    f"Data: {tarefa.data}, "
                    f"Prioridade: {tarefa.prioridade}, "
                    f"Status: {tarefa.status}"
                )
                self.view.mostrar_mensagem(mensagem)
        else:
            self.view.mostrar_mensagem('Nenhuma tarefa encontrada.')

    def atualizar_tarefa(self):
        tarefa_id = int(self.view.pegar_input('ID da tarefa a ser atualizada: '))
        tarefa = self.session.query(TarefaModel).filter_by(id=tarefa_id).first()

        if tarefa:
            descricao = self.view.pegar_input('Nova descrição (deixe em branco para manter): ')
            data_str = self.view.pegar_input('Nova data (AAAA-MM-DD, deixe em branco para manter): ')
            prioridade = self.view.pegar_input('Nova prioridade (alta, media, baixa, deixe em branco para manter): ')
            
            data = None
            if data_str:
                data = datetime.strptime(data_str, "%Y-%m-%d")
            
            tarefa.editar_tarefa(descricao, data, prioridade)
            self.session.commit()
            self.view.mostrar_mensagem('A tarefa foi atualizada com sucesso!')
        else:
            self.view.mostrar_mensagem('Tarefa não encontrada.')

    def excluir_tarefa(self):
        tarefa_id = int(self.view.pegar_input('ID da tarefa a ser excluída: '))
        tarefa = self.session.query(TarefaModel).filter_by(id=tarefa_id).first()

        if tarefa:
            self.session.delete(tarefa)
            self.session.commit()
            self.view.mostrar_mensagem('A tarefa foi excluída com sucesso!')
        else:
            self.view.mostrar_mensagem('Tarefa não encontrada.')
