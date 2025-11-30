# 1 - Considere o seguinte conjunto de números 1234 e as seguintes operações: (arrumei a ordem)
# push 1  
# push 2  
# pop → remove 2  
# push 3  
# push 4  
# pop → remove 4  
# pop → remove 3  
# pop → remove 1


def stack_operations():
    mainStack = [1,2,3,4]

    stack = []

    # push 1
    stack.append(mainStack[0])
    print(f"Pushed {mainStack[0]} onto stack.")

    # push 2
    stack.append(mainStack[1])
    print(f"Pushed {mainStack[1]} onto stack.")

    # pop → remove 2
    item = stack.pop()
    print(f"Popped {item} from stack.") 

    # push 3
    stack.append(mainStack[2])
    print(f"Pushed {mainStack[2]} onto stack.")

    # push 4
    stack.append(mainStack[3])
    print(f"Pushed {mainStack[3]} onto stack.")

    # pop → remove 4
    item = stack.pop()
    print(f"Popped {item} from stack.")

    # pop → remove 3
    item = stack.pop()
    print(f"Popped {item} from stack.")
    
    # pop → remove 1
    item = stack.pop()
    print(f"Popped {item} from stack.")


if __name__ == "__main__":
    stack_operations()