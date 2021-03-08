class Pesoa:

    olhos = 2
    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def estatico():
        return 42
    @classmethod
    def nomes_e_atibutos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'




if __name__ == '__main__':
    jonathan = Pesoa(nome='Jonathan')
    sueli = Pesoa(jonathan, nome='Jonathan')
    for filho in sueli.filhos:
        print(filho.nome)

print(Pesoa.nomes_e_atibutos_de_classe())