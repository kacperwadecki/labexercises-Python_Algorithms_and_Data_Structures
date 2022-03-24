from typing import Any, Callable, List
from binarytree import build, build2
from Queue import Queue


def horizontal_sum(tree: 'BinaryTree') -> List[int]:
    result: List[int] = []

    que: Queue = Queue()
    que.enqueue(tree.root)

    while len(que):
        qlen = len(que)
        sum = 0

        for i in range(qlen):
            act = que.dequeue()
            sum += act.value

            if act.left_child is not None:
                que.enqueue(act.left_child)
            if act.right_child is not None:
                que.enqueue(act.right_child)

        result.append(sum)
    return result


def visit(node) -> None:
    print(node)

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any, left_child: 'BinaryNode', right_child: 'BinaryNode') -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> Any:
        return self.value

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value, None, None)

    def add_right_child(self, value: Any) ->None:
        self.right_child = BinaryNode(value, None, None)

    def traverse_in_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self.value)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self.value)

    def traverse_pre_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        visit(self.value)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode) -> None:
        self.root = root;

    def traverse_in_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[['BinaryNode'], None]) -> None:
        self.root.traverse_pre_order(visit)


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



A: BinaryNode = BinaryNode(10, None, None)

tree: BinaryTree = BinaryTree(A)

A.add_left_child(9)
A.add_right_child(2)

A.left_child.add_left_child(1)
A.left_child.add_right_child(3)

A.right_child.add_left_child(4)
A.right_child.add_right_child(6)

A.left_child.right_child.add_right_child(20)
A.right_child.right_child.add_right_child(90)

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

tree.show()

print(horizontal_sum(tree))