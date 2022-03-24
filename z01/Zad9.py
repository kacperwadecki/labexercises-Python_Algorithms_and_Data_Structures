from typing import Dict


def zad9(x: int) -> str:
    di: Dict[int, str] = {
        1: 'poniedzialek',
        2: 'wtorek',
        3: 'sroda',
        4: 'czwartek',
        5: 'piatek',
        6: 'sobota',
        7: 'niedziela'
    }
    return di[x]

print(zad9(3))