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

queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2