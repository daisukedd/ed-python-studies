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

def is_palindrome(word):
    reversed_word = reverse_with_stack(word)
    return word == reversed_word

def main():
    word = input("Digite uma palavra: ").strip()
    print(is_palindrome(word))

if __name__ == "__main__":
    main()
