from typing import Optional

# --- Estrutura Base ---
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

    def get_height(self) -> int:
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node: TreeNode | None) -> int:
        if node is None:
            return 0
        
        # Calcula a altura de cada lado
        left_height = self._get_height_recursive(node.left)
        right_height = self._get_height_recursive(node.right)

        return max(left_height, right_height) + 1

if __name__ == "__main__":
    tree = BinaryTree()

    dados = [8, 3, 10, 1, 6, 14, 4, 7]
    
    for valor in dados:
        tree.insert(valor)

    altura = tree.get_height()
    print(f"Valores inseridos: {dados}")
    print(f"Altura da árvore esperada: 4")
    print(f"Altura calculada: {altura}")