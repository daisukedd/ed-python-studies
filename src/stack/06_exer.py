def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def reverse_list_with_stack(numbers):
    stack = []

    for num in numbers:
        push(stack, num)

    reversed_numbers = []
    while stack:
        reversed_numbers.append(pop(stack))

    return reversed_numbers

def main():
    numbers = [1, 2, 3, 4]
    result = reverse_list_with_stack(numbers)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
