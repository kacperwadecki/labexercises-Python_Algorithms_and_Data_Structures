from Zad1 import LinkedList
from typing import Any


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        result: str = ''
        act: Node = self._storage.head

        for i in range(len(self._storage) - 1, -1, -1):
            result += str(self._storage.node(at=i).data) + '\n'
        return result

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
       return self._storage.remove_last()

stack = Stack()
assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3

top_value = stack.pop()
assert top_value == 1

assert len(stack) == 2
print(stack)