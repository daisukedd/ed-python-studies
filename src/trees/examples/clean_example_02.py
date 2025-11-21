# Naming Convention e PEP 8
# Type Hinting e Docstrings
# Modularização de código em classes e métodos

from typing import Optional

class TreeNode:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


class BinarySearchTree:
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

    def search(self, value: int) -> bool:
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current: Optional[TreeNode], value: int) -> bool:
        if current is None:
            return False
        if value == current.value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def delete(self, value: int) -> None:
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if current is None:
            return None

        if value < current.value:
            current.left = self._delete_recursive(current.left, value)
        elif value > current.value:
            current.right = self._delete_recursive(current.right, value)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            successor_value = self._get_min_value(current.right)
            current.value = successor_value
            current.right = self._delete_recursive(current.right, successor_value)

        return current

    def _get_min_value(self, node: TreeNode) -> int:
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def get_height(self) -> int:
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return max(self._get_height_recursive(node.left), self._get_height_recursive(node.right)) + 1

    def print_in_order(self) -> None:
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, node: Optional[TreeNode]) -> None:
        if node:
            self._in_order_recursive(node.left)
            print(node.value, end=' ')
            self._in_order_recursive(node.right)


if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    for el in elements:
        bst.insert(el)

    print("In-order traversal (Initial):")
    bst.print_in_order()

    print(f"Tree Height: {bst.get_height()}")

    to_remove = 6
    print(f"\nRemoving value: {to_remove}")
    bst.delete(to_remove)

    print("In-order traversal (After removal):")
    bst.print_in_order()