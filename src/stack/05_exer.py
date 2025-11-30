# snake_case naming convention

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    stack = []
    
    while n > 0:
        remainder = n % 2
        push(stack, remainder)
        n //= 2

    binary = ""
    while stack:
        binary += str(pop(stack))

    return binary

def main():
    num = int(input("Digite um número decimal: "))
    print("Binário:", decimal_to_binary(num))

if __name__ == "__main__":
    main()
