def try_triple(i):
    'This function multiplies its argument by three'
    return i * 3


def try_square(i):
    'Computes the square of the arguments'
    return i ** 2


def main():
    for i in range(1, 11):
        a = try_triple(i)
        b = try_square(i)
        if b > a:
            break
        print(f'triple({i})=={a} square({i})=={b}')