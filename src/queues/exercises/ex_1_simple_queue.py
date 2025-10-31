class SimpleQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        print("Queue is empty!")
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def main():
    queue = SimpleQueue()

    print("Enter 5 numbers:")
    for _ in range(5):
        num = int(input("Number: "))
        queue.enqueue(num)

    print("\nRemoving and printing all elements in order:")
    while not queue.is_empty():
        value = queue.dequeue()
        print(value)


if __name__ == "__main__":
    main()


# # Example 

# queue = SimpleQueue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(300)

# print(queue.items)
# print("Dequeued:", queue.dequeue())
# print(queue.items)
# print("Is queue empty?", queue.is_empty())
# print("Queue size:", queue.size())

