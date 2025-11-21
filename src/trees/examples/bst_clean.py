from __future__ import annotations
from collections import deque
from typing import Generator, Optional


class TreeNode:

    __slots__ = ("value", "left", "right")

    def __init__(self, value: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, value: int) -> None:
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return

        parent = None
        current = self.root
        while current is not None:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        if value < parent.value:
            parent.left = node
        else:
            parent.right = node

    def search(self, value: int) -> bool:
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            current = current.left if value < current.value else current.right
        return False

    def in_order(self) -> Generator[int, None, None]:
        stack = []
        current = self.root
        while stack or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            yield current.value
            current = current.right

    def height(self) -> int:
        if self.root is None:
            return 0
        q = deque([self.root])
        levels = 0
        while q:
            levels += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return levels

    def min_value(self) -> Optional[int]:
        node = self.root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.value

    def max_value(self) -> Optional[int]:
        node = self.root
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.value

    def remove(self, value: int) -> None:

        def _remove(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if node is None:
                return None
            if val < node.value:
                node.left = _remove(node.left, val)
            elif val > node.value:
                node.right = _remove(node.right, val)
            else:
        
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                succ = node.right
                while succ.left is not None:
                    succ = succ.left
                node.value = succ.value
                node.right = _remove(node.right, succ.value)
            return node

        self.root = _remove(self.root, value)


if __name__ == "__main__":
    
    bst = BinarySearchTree()
    for chave in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(chave)

    print("Em ordem:", end=" ")
    print(*bst.in_order())
    print("Altura:", bst.height())
    print("Buscar 6:", bst.search(6))
    print("Menor:", bst.min_value(), "Maior:", bst.max_value())

    bst.remove(6)
    print("Após remover 6 — em ordem:", end=" ")
    print(*bst.in_order())
