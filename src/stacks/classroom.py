# Exemplo do Classroom

# funcoes para manipular a pilha
# empilha elemento no topo da pilha
def push(s, elemento):
    s.append(elemento)

def pop(s):
    # remove elemento no topo da pilha
    if not isempty(s):
        topo = s.pop()
        return topo
    
def isempty(s):
    return len(s) == 0

pilha = []
push(pilha, 1)
push(pilha, 4)
push(pilha, 6)
push(pilha, 7)
push(pilha, 8)
print(pilha)
print(pop(pilha))
print(pop(pilha))
print(pop(pilha))
print(pilha)



"""
def pop_par(s):
    if not isempty(s):
        valor = s.pop()
        if valor % 2 == 0:
            return valor
        else:
            return -1

def funcao_pilha(s):
    if not isempty(s):
        valor = s.pop()
        if valor % 2 == 0:
            return valor
        else:
            return -1
"""
# verifica se a pilha está vazia











"""




push(pilha_inversa,pop(pilha))
push(pilha_inversa,pop(pilha))
push(pilha_inversa,pop(pilha))
push(pilha_inversa,pop(pilha))
push(pilha_inversa,pop(pilha))
push(pilha_inversa,pop(pilha))
print(pilha)
print(pilha_inversa)
"""


"""pop(pilha)
print(pop(pilha))
valor = pop(pilha)
print(valor)
print(pilha)
valor = pop(pilha)
print(valor)
print(pilha)
valor = pop(pilha)
pop(pilha)
print(valor)
print(pilha)
print(pop(pilha))
print(pilha)

#print(valor)
#print(valor)
#pop(pilha)
#aux = pilha.pop()
#print(pilha.pop())
print(pilha)"""
"""pilha_letras = []
push(pilha_letras, 'a')
push(pilha_letras, 'b')
print(pilha_letras)
pop(pilha_letras)
print(pilha)
print(pilha_letras)
print("Removendo elemento e imprimindo somente valor par",
      pop_par(pilha))
print(pop_par(pilha))
print(pop_par(pilha))
print(pilha)
#pop(pilha)
#print(pop(pilha))
#print(pop(pilha))
#print(pilha)"""
