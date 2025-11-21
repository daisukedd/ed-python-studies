class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(current.right, value)

    def pre_order(self, node):
        if node:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=" ")

# Construindo a árvore
tree = BinarySearchTree()
for value in [7, 8, 3, 4, 2, 1, 6, 5]:
    tree.insert(value)

# Exibindo os percursos
print("Pré-ordem: ", end="")
tree.pre_order(tree.root)
print("\nEm-ordem: ", end="")
tree.in_order(tree.root)
print("\nPós-ordem: ", end="")
tree.post_order(tree.root)
