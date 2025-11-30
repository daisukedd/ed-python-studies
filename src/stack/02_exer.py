def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def print_stack(stack):
    print("Pilha final:", stack)

def print_even(stack):
    even_values = [x for x in stack if x % 2 == 0]
    print("Valores pares:", even_values)

def stack_operations():
    stack = []

    push(stack, 3)
    push(stack, 4)
    pop(stack)
    push(stack, 5)
    push(stack, 6)
    pop(stack)
    push(stack, 7)
    push(stack, 8)

    print_stack(stack)
    print_even(stack)

if __name__ == "__main__":
    stack_operations()
