def mainStack():
    sequence = [10,20, 30, 40, 50]
    stack = []

    for element in sequence:
        stack.append(element)
        print(stack)

    while len(stack) > 0:
        topStack = stack.pop()
        print("Top object:", topStack)
        print(stack)

if __name__ == '__main__':
    mainStack()
