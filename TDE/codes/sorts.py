def selection_sort(arr):
    arr = arr.copy()
    print("\nSELECTION SORT")

    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        # imprime só o estado atual principal
        print(f"Passo {i+1}: {arr}")

    print("Final:", arr)
    return arr



def quick_sort(arr):
    print("\nQUICK SORT")
    arr = arr.copy()
    passo = 1

    def quick(lst):
        nonlocal passo

        if len(lst) <= 1:
            return lst

        pivot = lst[0]
        menores = [x for x in lst[1:] if x <= pivot]
        maiores = [x for x in lst[1:] if x > pivot]

        print(f"Passo {passo}: pivot={pivot} | menores={menores} | maiores={maiores}")
        passo += 1

        return quick(menores) + [pivot] + quick(maiores)

    result = quick(arr)
    print("Final:", result)
    return result



def merge_sort(arr):
    print("\nMERGE SORT")
    arr = arr.copy()
    passo = 1

    def merge(lst):
        nonlocal passo

        if len(lst) <= 1:
            return lst

        meio = len(lst)//2
        esquerda = merge(lst[:meio])
        direita = merge(lst[meio:])

        res = []
        i = j = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                res.append(esquerda[i]); i += 1
            else:
                res.append(direita[j]); j += 1

        res.extend(esquerda[i:])
        res.extend(direita[j:])

        print(f"Passo {passo}: merge({esquerda}, {direita}) → {res}")
        passo += 1

        return res

    result = merge(arr)
    print("Final:", result)
    return result
