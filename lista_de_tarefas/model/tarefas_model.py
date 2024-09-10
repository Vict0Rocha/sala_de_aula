from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TarefaModel(Base):
    __tablename__ = 'tarefas'

    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    data = Column(Date)
    prioridade = Column(String)
    status = Column(String, default='pendente')

    def concluir_tarefa(self):
        self.status = 'concluida'

    def editar_tarefa(self, descricao=None, data=None, prioridade=None):
        if descricao:
            self.descricao = descricao
        if data:
            self.data = data
        if prioridade:
            self.prioridade = prioridade
