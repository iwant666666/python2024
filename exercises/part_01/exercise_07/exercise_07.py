import math


def triangle():
    x1 = float(input('Give base of the triangle:'))
    y1 = float(input('Give height of the triangle:'))
    print(f'The area is {0.5 * x1 * y1:.6f}')


def rectangle():
    x1 = float(input('Give width of the rectangle:'))
    y1 = float(input('Give height of the rectangle:'))
    print(f'The area is {x1 * y1:.6f}')


def circle():
    x1 = float(input('Give radius of the circle:'))
    print(f'The area is {math.pi * x1 ** 2:.6f}')


def main():
    while 1:
        x = input('Choose a shape(triangle,rectangle,circle): ')
        if x == "":
            break

        elif x == 'triangle':
            triangle()

        elif x == 'rectangle':
            rectangle()

        elif x == 'circle':
            circle()

        else:
            print('Unknown shape!')
