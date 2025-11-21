from typing import Optional, List

# Tree Node Definition and Type Hinting
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        # BST Insertion
        if not self.root:
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

    # Pre-order (Raiz -> Esquerda -> Direita)
    def get_pre_order(self) -> List[int]:
        return self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return [node.value] + self._pre_order_recursive(node.left) + self._pre_order_recursive(node.right)

    # In-order (Esquerda -> Raiz -> Direita)
    def get_in_order(self) -> List[int]:
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return self._in_order_recursive(node.left) + [node.value] + self._in_order_recursive(node.right)

    # Post-order (Esquerda -> Direita -> Raiz)
    def get_post_order(self) -> List[int]:
        return self._post_order_recursive(self.root)

    def _post_order_recursive(self, node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return self._post_order_recursive(node.left) + self._post_order_recursive(node.right) + [node.value]

if __name__ == "__main__":
    tree = BinaryTree()
    
    d = [8, 3, 10, 1, 6, 14, 4, 7]
    
    for value in d:
        tree.insert(value)

    print(f"Tree: {d}\n")
    
    print(f"1. Pre-order (R-E-D): {tree.get_pre_order()}")
    print(f"2. In-order  (E-R-D): {tree.get_in_order()}")
    print(f"3. Post-order (E-D-R): {tree.get_post_order()}")