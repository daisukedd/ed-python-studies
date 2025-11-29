from bst import *

codigos = [770, 875, 7, 59, 68, 682, 588, 67, 234, 411, 191, 512]

raiz = None

for codigo in codigos:
    raiz = insere(raiz, codigo)

print("\n--- (b) Pré-Ordem ---")
pre_ordem(raiz)

print("\n--- (c) Em Ordem ---")
em_ordem(raiz)

print("\n--- (d) Pós-Ordem ---")
pos_ordem(raiz)
