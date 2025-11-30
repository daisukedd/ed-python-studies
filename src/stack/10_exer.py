def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def merge_stacks_desc(stack1, stack2):
    result = []

    while stack1 or stack2:

        if not stack1:
            push(result, pop(stack2))
            continue

        if not stack2:
            push(result, pop(stack1))
            continue

        if stack1[-1] > stack2[-1]:
            push(result, pop(stack1))
        else:
            push(result, pop(stack2))

    return result


def main():
    stack1 = [5, 3, 1]  # topo = 1
    stack2 = [6, 4, 2]  # topo = 2

    merged = merge_stacks_desc(stack1, stack2)

    print("Pilha resultante (decrescente, topo = maior):", merged)

if __name__ == "__main__":
    main()
