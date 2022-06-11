#функция находит НОД(x, y) двух чисел

def nod(x, y):
    x, y = max(x, y), min(x, y)
    while x > 0 and y > 0:
        x, y = y, x % y
    return x

#функция находит НОК(x, y), строится на базе функции nod(x, y)
def nok(x, y):
    return x * y // nod(x, y)