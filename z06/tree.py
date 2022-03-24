from typing import Any, List, Callable, Union
from Queue import Queue

def visit(node: 'TreeNode') -> None:
    print(node.value)

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any, children: List['TreeNode']) -> None:
        self.value = value
        self.children = children
        self.parent = None

    def __str__(self) -> str:
        return self.value

    def is_leaf(self) -> bool:
        if self.children is None:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.value)
        if self.children:
            for child in self.children:
                child.print_tree()

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)

        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        fifo: Queue = Queue()

        for i in self.children:
            fifo.enqueue(i)

        while len(fifo) != 0:
            tmp: TreeNode = fifo.dequeue()
            visit(tmp)
            for i in tmp.children:
                fifo.enqueue(i)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self

        for i in self.children:
            if i.value == value:
                return i
            else:
                i.search(value)

class Tree:
    root: TreeNode

    def __init__(self, root: TreeNode) -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        kid: TreeNode = self.root.search(parent_name.value)
        kid.add(TreeNode(value, []))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)



wezel_A: TreeNode = TreeNode('A', [])
wezel_B: TreeNode = TreeNode('B', [])
wezel_C: TreeNode = TreeNode('C', [])
wezel_D: TreeNode = TreeNode('D', [])
wezel_E: TreeNode = TreeNode('E', [])
wezel_F: TreeNode = TreeNode('F', [])
wezel_G: TreeNode = TreeNode('G', [])
wezel_H: TreeNode = TreeNode('H', [])
wezel_I: TreeNode = TreeNode('I', [])

drzewo: Tree = Tree(wezel_F)

drzewo.root.add(wezel_B)
drzewo.root.add(wezel_G)

wezel_B.add(wezel_A)
wezel_B.add(wezel_D)

wezel_D.add(wezel_C)
wezel_D.add(wezel_E)

wezel_G.add(wezel_I)
wezel_I.add(wezel_H)

##drzewo.add('J', wezel_G)
##wezel_F.for_each_deep_first(visit)
##wezel_F.for_each_level_order(visit)

drzewo.root.print_tree()