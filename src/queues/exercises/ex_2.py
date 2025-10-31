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

def serve_customer(queue):
    if not queue.is_empty():
        customer = queue.dequeue()
        print(f"Serving customer: {customer}")
    else:
        print("No customers in queue.")

def main():
    service_queue = SimpleQueue()
    customers = ["Jax", "James", "Jinx", "Wander", "Evelyn"]

    for customer in customers:
        service_queue.enqueue(customer)

    while not service_queue.is_empty():
        serve_customer(service_queue)

if __name__ == "__main__":
    main()
