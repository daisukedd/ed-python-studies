def quick_sort(lista):
    # 1. Caso base:
    # Se a lista tiver 0 ou 1 elemento, ela já está ordenada.
    if len(lista) <= 1:
        return lista
    
    # 2. Escolha do pivô:
    # Vamos pegar o elemento central da lista como pivô.
    indice_meio = len(lista) // 2
    pivo = lista[indice_meio]
    
    # 3. Criação das três listas:
    # - menores: elementos menores que o pivô
    # - iguais: elementos iguais ao pivô
    # - maiores: elementos maiores que o pivô
    menores = []
    iguais = []
    maiores = []
    
    # 4. Separação dos elementos (particionamento)
    for elemento in lista:
        print(f"Analisando elemento:", elemento)
        if elemento < pivo:
            menores.append(elemento)
            print(f"Array 'menores' atual:", menores)
            print('Pivo atual:', pivo)
        elif elemento == pivo:
            iguais.append(elemento)
            print(f"Array 'iguais' atual:", iguais)
            print('Pivo atual:', pivo)
        else:
            maiores.append(elemento)
            print(f"Array 'maiores' atual:", maiores)
            print('Pivo atual:', pivo)
    
    # 5. Recursão:
    # Ordenamos apenas as listas 'menores' e 'maiores'
    # e depois juntamos tudo.
    return quick_sort(menores) + iguais + quick_sort(maiores)

print(quick_sort([8, 3, 5, 1, 9, 2]))