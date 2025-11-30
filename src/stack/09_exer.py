def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def factorial_with_stack(n):
    if n == 0:
        return 1

    stack = []

    while n > 0:
        push(stack, n)
        n -= 1

    result = 1

    while stack:
        result *= pop(stack)

    return result

def main():
    num = int(input("Digite um número: "))
    print("Fatorial:", factorial_with_stack(num))

if __name__ == "__main__":
    main()
