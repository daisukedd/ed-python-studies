from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: TreeNode, value: int) -> None:
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
            else:
                self._insert_recursive(current.right, value)

    def get_total_sum(self) -> int:
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        
        return node.value + self._sum_recursive(node.left) + self._sum_recursive(node.right)

if __name__ == "__main__":
    tree = BinaryTree()
    
    dados = [8, 3, 10, 1, 6, 14, 4, 7]
    
    for valor in dados:
        tree.insert(valor)

    total = tree.get_total_sum()
    print(f"Valores inseridos: {dados}")
    print(f"Soma total esperada: 53")
    print(f"Soma total calculada: {total}")