
class Personagem:
    def __init__(self, nome, dinheiro):
        self.nome = ("name_x")
        self.dinheiro = 1000

    def move_direita(self):
        self.dinheiro = self.dinheiro - 10 
        print("seu personagem utilizou $10")

    def move_esquerda(self):
        self.dinheiro = self.dinheiro - 10
        print("seu personagem utilizou $10")
    