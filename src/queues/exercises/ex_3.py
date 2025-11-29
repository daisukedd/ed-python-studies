def reverse_queue(queue):
    reversed_queue = []
    while len(queue) > 0:
        element = queue.pop(0)
        reversed_queue.insert(0, element)
    return reversed_queue

# Example
# In Python, the .copy() method, when used with mutable data structures like lists and dictionaries, creates a shallow copy

my_queue = [1, 20, 300, 4000, 5]
reversed_queue = reverse_queue(my_queue.copy())
print("Original Queue:", my_queue)
print("Reversed Queue:", reversed_queue)