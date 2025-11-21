class NodoArvore:

    def __init__(self, chave,
                 esquerda=None,
                 direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

def insere(raiz, nodo):

    if raiz is None:
        raiz = nodo

    # Nodo deve ser inserido na subárvore direita.
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore esquerda.
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

def busca(raiz, chave):

    if raiz is None:
        return None

    if raiz.chave == chave:
        print(raiz.chave)
        return raiz

    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    else:
        return busca(raiz.esquerda, chave)

def em_ordem(raiz):
    if raiz is None:
        return

    em_ordem(raiz.esquerda)

    print(raiz.chave)

    em_ordem(raiz.direita)

def pre_ordem(raiz):
    if raiz is None: #if not raiz:
        return
    print(raiz.chave)

    pre_ordem(raiz.esquerda)
    pre_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return

    
    pos_ordem(raiz.esquerda)
    pos_ordem(raiz.direita)
    print(raiz.chave)

arvore = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(arvore, nodo)

print("Em ordem")
print("Pos-ordem")
pos_ordem(arvore)
resultado = busca(arvore,40)
if resultado:
    print("Valor encontrado")
    
else:
   print("Valor nao encontrado")