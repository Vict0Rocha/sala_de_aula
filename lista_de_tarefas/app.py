import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from controller.tarefas_controller import TarefaController
from model.tarefas_model import Base
from view.tarefas_view import TarefaView

def main():
    db_path = 'tarefas.db'
    engine = create_engine(f'sqlite:///{db_path}')

    if not os.path.exists(db_path):
        Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    view = TarefaView()
    controller = TarefaController(session, view)

    while True:
        print("\nMenu")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Excluir Tarefa")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            controller.adicionar_tarefa()
        elif escolha == '2':
            controller.listar_tarefas()
        elif escolha == '3':
            controller.atualizar_tarefa()
        elif escolha == '4':
            controller.excluir_tarefa()
        elif escolha == '6':
            break
        else:
            print("Opção inválida, tente novamente")

if __name__ == "__main__":
    main()
