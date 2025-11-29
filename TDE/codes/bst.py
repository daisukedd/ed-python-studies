# Reaproveitamento de código de:

class NodoArvore:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None


def insere(raiz, chave):
    if raiz is None:
        return NodoArvore(chave)

    if chave < raiz.chave:
        raiz.esquerda = insere(raiz.esquerda, chave)
    else:
        raiz.direita = insere(raiz.direita, chave)

    return raiz


def pre_ordem(raiz):
    if raiz:
        print(raiz.chave)
        pre_ordem(raiz.esquerda)
        pre_ordem(raiz.direita)


def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esquerda)
        print(raiz.chave)
        em_ordem(raiz.direita)


def pos_ordem(raiz):
    if raiz:
        pos_ordem(raiz.esquerda)
        pos_ordem(raiz.direita)
        print(raiz.chave)
