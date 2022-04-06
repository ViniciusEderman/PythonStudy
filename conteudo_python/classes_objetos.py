## exemplo de classe 

class Avatar:
    def __init__(self, nome, energia):
        self.nome = nome 
        self.energia = energia 

    def mov_right(self):
        print('Move-se a direita')

    def mov_lefy(self):
        print('Move-se a esquerda')
    
    def alimentar(self):
        self.energia += 5
        print('Alimentando o seu personagem... wait a second')
        print('...')
        print('Energia restabelicida.')

#finished