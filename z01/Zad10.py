def zad10(text: str) -> bool:
    result: str = ''

    for i in range(len(text)):
        result += (text[len(text) - i - 1])

    if result == text:
        return True
    return False

print(zad10('alad'))