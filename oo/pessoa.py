class Pesoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    jonathan = Pesoa(nome='Jonathan')
    sueli = Pesoa(jonathan, nome='Jonathan')
    for filho in sueli.filhos:
        print(filho.nome)

