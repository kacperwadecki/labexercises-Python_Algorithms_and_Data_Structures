from typing import List


def Zad7(lista: List) -> tuple:
    return tuple(lista)

li1: List = []

for i in range(5):
    x: int = int(input("Podaj liczbe: "))
    li1.append(x)

print(li1)
print(Zad7(li1))