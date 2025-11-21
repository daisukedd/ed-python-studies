class NodeTree:
    def __init__(self, key, left=None, right=None):
        self.value = key
        self.left = left
        self.right = right

    def insert(raiz, node):
        if raiz is None:
            return node
        if node.value < raiz.value:
            raiz.left = NodeTree.insert(raiz.left, node)   
        else:
            raiz.right = NodeTree.insert(raiz.right, node)  
        return raiz

    def pre_order(raiz):
        if raiz:
            print(raiz.value, end=" ")
            NodeTree.pre_order(raiz.left)   
            NodeTree.pre_order(raiz.right)  

    def in_order(raiz):
        if raiz:
            NodeTree.in_order(raiz.left)    
            print(raiz.value, end=" ")
            NodeTree.in_order(raiz.right)   
    
    def post_order(raiz):
        if raiz:
            NodeTree.post_order(raiz.left)   
            NodeTree.post_order(raiz.right)  
            NodeTree.post_order(raiz.left)   
            print(raiz.value, end=" ")


valuesTree = [7, 8, 3, 4, 2, 1, 6, 5]
root = NodeTree(valuesTree[0])

for value in valuesTree[1:]:
    node = NodeTree(value)
    root = NodeTree.insert(root, node)

print("Pré-ordem: ", end="")
NodeTree.pre_order(root)
print("\nEm-ordem: ", end="")
NodeTree.in_order(root)
print("\nPós-ordem: ", end="")
NodeTree.post_order(root)
