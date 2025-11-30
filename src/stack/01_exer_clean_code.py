def push(stack, item):
    stack.append(item)
    print(f"Pushed {item} onto stack.")

def pop(stack):
    item = stack.pop()
    print(f"Popped {item} from stack.")
    return item

def stack_operations():
    values = [1, 2, 3, 4]
    stack = []

    push(stack, values[0])  # push 1
    push(stack, values[1])  # push 2
    pop(stack)              # pop → remove 2
    push(stack, values[2])  # push 3
    push(stack, values[3])  # push 4
    pop(stack)              # pop → remove 4
    pop(stack)              # pop → remove 3
    pop(stack)              # pop → remove 1


if __name__ == "__main__":
    stack_operations()