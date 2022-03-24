from typing import Any


class Node:
    data: Any
    next: 'Node'

    def __init__(self, data=None, next=None) -> None:
        self.data: Any = data
        self.next: Node = next


class LinkedList:
    head: Node
    tail: Node
    def __init__(self) -> None:
        self.head: Node = None
        self.tail: Node = None

    def __str__(self) -> str:
        act: Node = self.head
        result: str = ''

        if self.head is None:
            print("Lista jest pusta")
            return ''

        while act:
            result += str(act.data)
            if act.next: result += ' -> '
            act = act.next
        return result

    def __len__(self) -> int:
        act: Node = self.head
        count: int = 0

        while act:
            act = act.next
            count += 1
        return count

    def push(self, data: Any) -> None:
        node: Node = Node(data, self.head)

        if self.head == None:
            self.head: Node = node
            self.tail = self.head
        else:
            self.head = node

    def append(self, data: Any) -> None:
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            return

        act: Node = self.head
        while act.next:
            act = act.next

        act.next = Node(data, None)
        self.tail = act.next

    def node(self, at: int) -> Node:
        if at < 0 or at >= self.__len__():
            raise Exception("Cos poszlo nie tak")

        act: Node = self.head

        for i in range(at):
            act = act.next
        return act

    def insert(self, data: Any, after: Node) -> None:
        act: Any = self.head

        while act != after:
            act = act.next

        if act.next == None:
            act.next = Node(data, None)
            self.tail = act.next
        else:
            act.next = Node(data, act.next)

    def pop(self) -> Any:
        if self.head is None:
            raise Exception("Cos poszlo nie tak")

        if len(self) == 1:
            self.tail = None

        result: Any = self.head.data
        self.head = self.head.next
        return result

    def remove_last(self) -> Any:
        if self.head is None:
            raise Exception("Cos poszlo nie tak")

        if len(self) == 1:
            return self.pop()

        act: Node = self.head
        result: Any

        while act.next.next != None:
            act = act.next
        result: Any = act.next.data
        self.tail = act
        act.next = None
        return result

    def remove(self, after: Node) -> None:
        if self.head is None:
            raise Exception("Cos poszlo nie tak")

        act: Node = self.head
        tmp: int = 0

        while act != after:
            act = act.next
            tmp += 1
        if tmp == len(self) - 1:
            raise Exception("Cos poszlo nie tak")

        if act.next == self.tail:
            self.tail = act

        act.next = act.next.next


list_ = LinkedList()
assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.data == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.data == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'