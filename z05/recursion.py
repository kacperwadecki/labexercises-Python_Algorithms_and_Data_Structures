from typing import List
import math
import numpy as np

def numbers(n: int) -> None:
    print(n);
    n -= 1
    if n < 0:
        return
    numbers(n)

def fib(n: int) -> None:
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return number
    else:
        return(number * power(number, n-1))

def reverse(txt: str) -> str:
    if len(txt) == 0:
        return txt
    else:
        return reverse(txt[1:]) + txt[0]

def factorial(n: int) -> int:
    if n <=1:
        return 1
    else:
        return (n * factorial(n-1))

def prim(n: int, i: int = 2) -> bool:
    if n == 1: return False
    elif i == n: return True
    elif n % i == 0: return False
    return prim(n, i + 1)

def n_sums(n: int) -> List[int]:
    k: int = 1
    l: int = 1
    li: List = []

    for i in range(n):
        k *= 10
        if i > 0:
            l *= 10
    k -= 1

    for i in range(k + 1):
        sumaP: int = 0
        sumaNP: int = 0
        tmp: int = i
        flaga: bool = True

        if i >= l:
            while tmp >= 10:
                if flaga:
                    sumaP += tmp % 10
                    tmp /= 10
                    tmp = math.floor(tmp)
                    flaga = False
                elif flaga == False:
                    sumaNP += tmp % 10
                    tmp /= 10
                    tmp = math.floor(tmp)
                    flaga = True

            if flaga: sumaP += tmp
            elif flaga == False: sumaNP += tmp
            if sumaP == sumaNP:
                li.append(i)
    return li

def existsIn(x: int, li: List) -> bool:
    for i in li:
        if i == x: return True
    return False

def combinations_True(li: List) -> bool:
    li2: List = []
    for i in range(len(li)):
        if not existsIn(li[i], li2):
            if li[i] != li[i + li[i] + 1] or li[i] == 0:
                return False
            li2.append(li[i])
    return True

def zero_Li(li: List[int]) -> List[int]:
    for i in range(len(li)):
        li[i] = 0
    return li

def same_number(li1: List[int], li2: List[int]) -> bool:
    for i in range(len(li1)):
        if li1[i] != 0 and li2[i] != 0:
            return False
        return True

def change(li: List[int], x) -> List[int]:
    for i in range(len(li)):
        if li[i] == x:
            li[i] = 0
    return li

def getIndex(li: List[int], x) -> int:
    result: int = 0
    for i in range(len(li)):
        result += 1
        if li[i] == x:
            return result

def combinations(n: int) -> List[List[int]]:
    li1: List[int] = []
    li_result: List[List[int]] = []

    tmp1: int = 1
    start_index = 0
    idx: int = 0
    tmp2: bool = True

    for i in range(n * 2):
        li1.append(0)

    while not combinations_True(li1):
        while start_index + tmp1 + 1 < len(li1):
            if  li1[start_index] == 0 and li1[start_index + tmp1 + 1] == 0:
                li1[start_index] = tmp1
                li1[start_index + tmp1 + 1] = tmp1
                tmp1 += 1
                start_index = 0

            else:
                start_index += 1

        if not combinations_True(li1):
            tmp1 -= 1
            idx = getIndex(li1, tmp1)
            start_index = idx
            li1 = change(li1, tmp1)

    li_result.append(li1)
    return li_result

def remove_duplicates(txt: str) -> str:
    result: str = ''
    tmp1: Any = 10

    for i in txt:
        if tmp1 != i:
            result += i
            tmp1 = i
    return result

print(combinations(5))