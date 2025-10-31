class Queue:
    def __init__(self, size):
        self.queue = [0] * size
        self.start = 0
        self.end = 0

    def insert(self, element):
        if self.end < len(self.queue):
            self.queue[self.end] = element
            self.end += 1
        else:
            print("Queue is full")

    def remove(self):
        if not self.is_empty():
            value = self.queue[self.start]
            self.queue[self.start] = None
            self.start += 1
            return value
        print("Queue is empty")

    def is_empty(self):
        return self.start == self.end

    def show(self):
        return self.queue[self.start:self.end]

Queue_size = 5
simple_queue = Queue(Queue_size)
simple_queue.show()  # []
simple_queue.insert(10)
simple_queue.insert(20)
simple_queue.insert(30)
simple_queue.show()  # [10, 20, 30]
simple_queue.remove()  # 10
simple_queue.show()  # [20, 30]
simple_queue.insert(40)

simple_queue.show()  # [20, 30, 40]