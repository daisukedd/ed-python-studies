class CustomerQueue:
    def __init__(self):
        self.queue= []

    def customer_arrives(self, customer_name):
        self.queue.append(customer_name)
        print(f"Customer {customer_name} has arrived and joined the queue.")

    def serve_next_customer(self):
        if self.queue:
            serverd = self.queue.pop(0)
            print(f"Serving customer: {serverd}")
        else:
            print("No customers in queue.")


def simulate_store_queue():
    store_queue = CustomerQueue()

    store_queue.customer_arrives("Jinx")
    store_queue.customer_arrives("Jax")
    store_queue.customer_arrives("Xin Zhao")
    store_queue.customer_arrives("Rammus")
    store_queue.customer_arrives("Pyke")

    while store_queue.queue:
        store_queue.serve_next_customer()
    
    print("All customers have been served!!!")

    # CleanCode bolaado aqui - não finalizei!

    # queue = CustomerQueue()

    # customers = ["Jinx", "Jax", "Xin Zhao", "Rammus", "Pyke"]
    # for customer in customers:
    #     queue.customer_arrives(customer)

    # while not queue.is_empty():
    #     queue.serve_next_customer()

    # print("All customers have been served!!!")


if __name__ == "__main__":
    simulate_store_queue()