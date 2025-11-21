# Exemplo disponivel no Classrom

class NodoArvore:

    def __init__(self, valor,
                 esquerda=None,
                 direita=None):
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita

def insere(raiz, nodo):
        """Insere um nodo em uma árvore binária de pesquisa."""
        # Nodo deve ser inserido na raiz.
        if raiz is None:
            raiz = nodo
        # Nodo deve ser inserido na subárvore direita.
        elif nodo.valor > raiz.valor:
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

#esquerda - raiz - direita
def em_ordem(raiz):
    if raiz is None:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.valor,end=' ')
    

    # Visita filho da direita.
    em_ordem(raiz.direita)

# Calcula a altura da árvore em NÍVEIS
def altura(raiz):
    if raiz is None:
        return 0  # Árvore vazia tem altura 0 (sem níveis)
    
    altura_esquerda = altura(raiz.esquerda)
    altura_direita = altura(raiz.direita)

    return max(altura_esquerda, altura_direita) +1 

def buscar(raiz, valor):
    if raiz is None:
        return False
    if valor == raiz.valor:
        return True
    elif valor < raiz.valor:
        return buscar(raiz.esquerda, valor)
    else:
        return buscar(raiz.direita, valor)


def menor_valor(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.valor

def maior_valor(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.valor


def remover(raiz, valor):
        # Caso base: árvore vazia
        if raiz is None:
            return raiz

        # 1 - Procurar o nó a ser removido
        if valor < raiz.valor:
            raiz.esquerda = remover(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = remover(raiz.direita, valor)
        else:
            #Encontramos o nó a remover

            # 2 - Caso 1: Nó sem filhos (folha)
            if raiz.esquerda is None and raiz.direita is None:
                return None

            # 3 - Caso 2: Um filho apenas
            elif raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda

            # 4 - Caso 3: Dois filhos
            # Encontrar o menor nó da subárvore direita (sucessor)
            sucessor = minimo(raiz.direita)
            raiz.valor = sucessor.valor
            # Remover o sucessor da subárvore direita
            raiz.direita = remover(raiz.direita, sucessor.valor)

        return raiz

def minimo(no):
    atual = no
    while atual.esquerda is not None:
        atual = atual.esquerda
    return atual





#[40, 20, 60, 50, 70, 10, 30]:
#[ 33, 15, 41, 38, 34, 47, 43,49]
#arvore = NodoArvore(40)
#for chave in [20, 60, 50, 70, 10, 30]:

arvore = NodoArvore(8)  # criar o no raiz
for chave in [3,10,1,6,14,4,7,13]:  #[2, 1, 4, 5, 8, 10,7]:
    nodo = NodoArvore(chave)
    insere(arvore, nodo)

#arvore = NodoArvore(33)  # criar o no raiz
#for chave in [15, 41, 38, 34, 47, 43, 49]:
#    nodo = NodoArvore(chave)
#    insere(arvore, nodo)

em_ordem(arvore) 
raiz = remover(arvore,6)
print("")
em_ordem(arvore) 
print("")
print("Altura da arvore" ,altura(arvore)) 
#print("Buscar 10:", buscar(arvore, 10))
#print("Buscar 20:", buscar(arvore, 20))
#print("Menor valor", menor_valor(arvore))
#print("Maior valor", maior_valor(arvore))
