from typing import Any, List
from binarytree import build
from Queue import Queue

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child: 'BinaryNode', right_child: 'BinaryNode') -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def min(self) -> 'BinaryNode':
        if self.left_child < self.right_child:
            return self.left_child
        return self.right_child

    def listValues_levelorder(self) -> List[int]:
        queue: List[BinaryNode] = []
        result: List[int] = []

        queue.append(self)

        while (len(queue) > 0):

            result.append(queue[0].value)
            node = queue.pop(0)

            if node.left_child is not None:
                queue.append(node.left_child)

            if node.right_child is not None:
                queue.append((node.right_child))
        return result

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self,node: BinaryNode, val: Any) -> BinaryNode:
        if val < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(val, None, None)
            else:
                node.left_child = self._insert(node.left_child, val)
        if val >= node.value:
            if node.right_child is None:
                node.right_child = BinaryNode(val, None, None)
            else:
                node.right_child = self._insert(node.right_child, val)
        return node


    def insertlist(self, list: List[Any]) -> None:
        for i in list:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        tmp: List[int] = self.root.listValues_levelorder()
        for i in tmp:
            if i == value:
                return True
        return False

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node == None:
            return node
        if value == node.value:

            if node.left_child == None:
                node = node.right_child
            elif node.right_child == None:
                node = node.left_child
            else:
                node.right_child = self._remove(node.right_child, node.value)
        elif value < node.value:
            node.left_child = self._remove(node.left_child, value)
        else:
            node.right_child = self._remove(node.right_child, value)

        return node

    def show(self) -> None:
        que: Queue = Queue()
        result: List[int] = []

        que.enqueue(self.root)

        while len(que):
            node = que.dequeue()
            if node is not None:
                result.append(node.value)
            else:
                result.append(None)

            if node is not None:
                que.enqueue(node.left_child)
                que.enqueue((node.right_child))

        binary_tree = build(result)
        print(binary_tree)

A: BinaryNode = BinaryNode(8, None, None)

tree: BinarySearchTree = BinarySearchTree(A)

tree.insertlist([10,14,13,3,1,6,4,7])

tree.remove(1)
tree.show()
