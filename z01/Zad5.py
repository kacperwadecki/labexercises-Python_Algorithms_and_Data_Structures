def division(x: float, y:float) -> float:
    if x > 0 and y > 0 and y != 0:
        return x / y
    return "Liczby są ujemne lub w mianowniku mamy 0"

print(division(3,0))