class Direcao:
    rotacao_a_direita_dict = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE:NORTE
    }
    rotacao_a_esquerda_dict = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE:SUL
    }


    def  __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]
    def girar_a_direita(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]


NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


