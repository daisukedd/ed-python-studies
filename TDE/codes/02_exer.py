P1 = [40,30,25,10]
P2 = [34,60,28,15]
P3 = [20,35]

A1 = []
A2 = []

def push(stack, value):
    stack.append(value)

# Remove element from top of stack
def pop(stack):
    return stack.pop() if stack else None

def show_stack(P1,P2,P3):
    A1 = []
    A2 = []

    while P1 or P2:
        if P1:
            push(A1, pop(P1))
        if P2:
            push(A2, pop(P2))

    while P3:
        push(A1, pop(P3))
    while A1:
        push(A2, pop(A1))

    for _ in range(4):
        print(pop(A2))

show_stack(P1,P2,P3)
