def mainStack():
    sequence = [1,2,5,6,7,12,15,18,20]
    stack = []
    for item in sequence:
        stack.append(item)
        print(f"Pushed {item} onto stack.")
    while len (stack) > 0:
        item = stack.pop()
        print(f"Popped {item} from stack.")
        print(f"Current stack: {stack}")

if __name__ == "__main__":
    mainStack()