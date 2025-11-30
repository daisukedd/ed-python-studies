def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def sort_stack(stack):
    aux = []  # pilha auxiliar
    
    while stack:
        current = pop(stack)

        while aux and aux[-1] > current:
            push(stack, pop(aux))

        push(aux, current)
    return aux  

def main():
    stack = [4, 1, 3, 2]  
    sorted_stack = sort_stack(stack)
    
    print("Pilha ordenada:", sorted_stack)

if __name__ == "__main__":
    main()
