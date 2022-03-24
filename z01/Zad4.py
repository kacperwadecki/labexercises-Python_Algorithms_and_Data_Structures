def zad2(name: str, sname: str) -> str:
    return name[0].upper() + '.' + sname[0].upper() + sname[1:]

def zad4(name: str, sname: str, function) -> str:
    return function(name, sname)

print(zad4('jan','kowalski',zad2))