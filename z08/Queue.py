from LinkedList import LinkedList
from typing import Any


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def __str__(self) -> str:
        act: Node = self._storage.head
        result: str = ''

        while act:
            result += str(act.data)
            if act.next: result += ', '
            act = act.next
        return result

    def __len__(self) -> None:
        return len(self._storage)

    def peek(self) -> Any:
        return self._storage.head.data

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

