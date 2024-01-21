import math


def area():
    A = input('input the length of triangle（seperated them by\';\', for example: 12;12;12 ）: ')
    list1 = list(map(int,A.split(';')))
    p = sum(list1)/2
    q = math.sqrt(p*(p-list1[0])*(p-list1[1])*(p-list1[2]))
    print('the triangle area is:',q)

# def sum_of_squares(a, b):
#     "Computes the sum of arguments squared"
#     return a ** 2 + b ** 2
# print(sum_of_squares(3, 4))

def length(*t, degree=2):
    """Computes the length of the vector given as parameter. By default, it computes
    the Euclidean distance (degree==2)"""
    s=0
    for x in t:
        s += abs(x)**degree
    return s**(1/degree)

def just_try_4():
    #count = 0
    result = []
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        for j in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            print('{:3d}'.format(i*j),end= ' ')
            result.append(i*j)
            if len(result)%10 ==0:
                print(end='\n')

            # count += 1
            # if (count%10 == 0):

def just_try_5():
    pair = ()
    for i in [1, 2, 3, 4, 5, 6]:
        for j in [1, 2, 3, 4, 5, 6]:
            pair += (i, j)
            if i+j != 5:
                continue
            print('({},{})'.format(i, j))

def just_try_6():
    # def triple(i):
    #     for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    #         s = i*3
    #     return s
    # def square(i):
    #     for i in range(1,11):
    #         t = i**2
    #     return t
    # print(f'triple({i})=={s}', f'square({i})=={t}')
    # print(triple(3))
    # print(square(5))
    def triple(t):
        a = t * 3
        return a

    def square(s):
        a = s ** 2
        return a

    for i in range(1, 11):
        t = triple(i)
        s = square(i)
        if s>t:
            break
        print(f" triple({i})=={t} square({i})=={s}")


def just_try_7():
    def triangle():
        x1 = input('Given base of the triangle: ')
        x2 = input('Given height of the triangle: ')
        return 0.5 * float(x1) * float(x2)

    def rectangle():
        y1 = input('Given base of the rectangle: ')
        y2 = input('Given height of the rectangle: ')
        return float(y1) * float(y2)

    def circle():
        r = input('Give radius of the circle: ')
        return math.pi*float(r)**2

    x = input('Choose a shape (triangle,rectangle,circle): ')
    if x == 'triangle':
        print('The area is', format(triangle(),'.6f'))
    elif x == 'rectangle':
        print('The area is', format(rectangle(), '.6f'))
    elif x == 'circle':
        print('The area is', format(circle(), '.6f'))
    else:
        print('Unknown shape!')

def just_try_8():
    def slove_quadratic(a,b,c):
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a))/(2*a)
        return (x1, x2)

# def merge(L1, L2):
#     new = []
#     L = L1+L2
#     while len(L) > 0:
#         a = min(L)
#         new.append(a)
#         L.remove(a)
#         # while len(L)<0:
#         #     break
#     return new
# print(merge([1,5,7],[2,4,6]))

def detect_ranges(L):
    new_list = []
    sorted_L = sorted(L)
    while len(sorted_L) > 0:
        for i in range(len(sorted_L[:-1])):
            if sorted_L[i+1] - sorted_L[i] != 1:
                break
            new_list.append(sorted_L[i])
        else:
            continue
        new_list.extend('({},{})'.format(sorted_L[i],sorted_L[i+1]))
    return new_list

print(detect_ranges([2, 5, 4, 8, 12, 6, 7, 10, 13]))
