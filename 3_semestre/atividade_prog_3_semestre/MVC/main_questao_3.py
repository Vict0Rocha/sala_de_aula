''' Questão 3
Sistema de gerenciamento de estudantes com MVC e atributos de classe
'''
from estudantes_model import Estudantes
from estudante_view import EstudantesView
from estudante_controller import EstudanteController

# Criando uma instância do controlador com a visualização
view = EstudantesView()
controller = EstudanteController(view)

# Adicionando alguns estudantes
controller.adicionar_estudante(1, "Victor", 19)
controller.adicionar_estudante(2, "Henrique", 22)
controller.adicionar_estudante(3, "Leonardo", 19)

# Exibindo os detalhes de todos os estudantes
print("Detalhes dos Estudantes (Antes da Atualização)")
controller.exibir_detalhes_estudantes()

# Atualizando o nome e a idade de um estudante específico
controller.atualiza_nome(2, "Roberto")
controller.atualiza_idade(2, 25)
controller.atualiza_idade(1, 20)

# Exibindo novamente os detalhes dos estudantes para verificar as mudanças
print("\nDetalhes dos Estudantes (Após a Atualização)")
controller.exibir_detalhes_estudantes()
