# Clean Code Exercise: Stack Implementation to Reverse a String

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

def reverse_with_stack(text):
    stack = []

    for char in text:
        push(stack, char)

    reversed_text = ""
    while stack:
        reversed_text += pop(stack)

    return reversed_text

def main():
    user_input = input("Digite uma string: ")
    inverted = reverse_with_stack(user_input)
    print("String invertida:", inverted)

if __name__ == "__main__":
    main()
