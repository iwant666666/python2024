import math

def statement():
    x = input('Give an integer: ')
    x = int(x)
    if x >= 0:
        a = x
    else:
        a = -x
        print('The absolute value of %i is %i' % (x,a))

    c = float(input('Give a number: '))
    if c > 0:
        print('c is positive')
    elif c < 0:
        print('c is negative')
    else:
        print('c is zero')

    l = [1,3,65,3,-1,56,-10]
    for x in l:
        if x < 0:
            break
    print('The first negative list element was',x)


def continuing_loop():
    from math import sqrt,log
    l = [1,3,65,3,-1,56,-10]
    for x in l:
        if x < 0:
            continue
        print(f'Square root of {x} is {sqrt(x):.3f}')
        print(f'Natural logarithm of {x} is {log(x):.4f}')


def named(a,b,c):
    print('First:',a,'Second:',b,'Third:',c)


def using_zip():
    days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
    weathers = "rainy rainy sunny cloudy rainy sunny sunny".split()
    temperatures = [10, 12, 12, 9, 9, 11, 11]
    # Or equivalently:
    # for day, weather, temperature in zip(days, weathers, temperatures):
    #     print(f"On {day} it was {weather} and the temperature was {temperature} degrees celsius.")

    for t in zip(days, weathers, temperatures):
        print("On {} it was {} and the temperature was {} degrees celsius.".format(*t))


# Example for lists methods:
def modifying_lists():
    # 1. Using append()
    numbers = [21, 34, 54, 12]

    print("Before Append:", numbers)

    # using append method
    numbers.append(32)

    print("After Append:", numbers)

    print()

    # 2. Using extend()
    numbers = [1, 3, 5]

    even_numbers = [4, 6, 8]

    print("Before Extend:", numbers)

    # add elements of even_numbers to the numbers list
    numbers.extend(even_numbers)

    print("List after Extend:", numbers)

    print()

    # 3. Using insert()
    numbers = [10, 30, 40]

    print("Before Insert:", numbers)

    # insert an element at index 1 (second position)
    numbers.insert(1, 20)

    print("List after Insert:", numbers)  # [10, 20, 30, 40]

    print()

    # More example here: https://www.programiz.com/python-programming/methods/list

    L = [11, 13, 22, 32]
    L = range(3)
    print("range:", L)
    print()

    L = [5, 3, 7, 1]
    print("Sorted:", L, sorted(L, reverse=True))


def enumerate_example():
    L = [1, 2, 98, 5]
    keys = ["check", "look", "try", "pop"]
    counter = 0
    for i, x in enumerate(L):
        print(i, x)
    dic = {key: list(L) for key in keys}
    dic2 = dict(zip(keys, L))
    print(dic, dic2)


def reduce_example():
    L = list(range(1, 11))
    from functools import reduce  # import the reduce function from the functools module
    r = reduce(lambda x, y: x + y, L)
    print(r)


def quick_sort(lst):
    if len(lst) <= 1:
        print("return", lst)
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    print(pivot, left, middle, right)
    return quick_sort(left) + middle + quick_sort(right)


def ex1_9notes():
    print(quick_sort([1, 5, 9, 12, 2, 6, 10, 5, 3, 7, 1, 10]))


# zipping sequences
def zipping_sequences():
    L1=[1,2,3]
    L2=["first", "second", "third"]
    print(zip(L1, L2))
    print(list(zip(L1, L2)))

    days = 'Monday Tuesday Wednsday Thursday Friday Saturday Sunday'.split()
    # print(days)
    weathers = 'rainy rainy sunny cloudy rainy sunny sunny'.split()
    temperatures=[10,12,12,9,9,11,11]
    for day, weather, temperature in zip(days,weathers,temperatures):
        print(f'On {day} it was {weather} and the temperature was {temperature} degrees celsius.')

def string_type():
    s = "abcdefg"
    for i in range(4):
        print(s[i])
    print({s[1:4]})
    print({s[0:4]})


