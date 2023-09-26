class Pomba:
    # Criar os atributos
    def __init__(self, color, is_sick, heigth_fly):
        self.color = color
        self.is_sick = is_sick
        self.height_fly = heigth_fly

    # Criar os metodos
    def cagar(self, sick):
        if sick:
            print("Cagando mole!")
        else:
            print("Cagando duro")

    def fly(self):
        if self.height_fly >= 500:
            self.cagar(self.is_sick)
        else:
            print("A pomba não ira cagar")
