import math

def circle(radius):
    return math.pi * radius ** 2

def rectangle(lenth,width):
    return lenth * width

def triangle(base,height):
    return 0.5 * base * height

def square(side):
    return side ** 2


def parallelogram(base, height):
    return base * height


def pentagon(side):
    return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2


def hexagon(side):
    return (3 * math.sqrt(3) * side ** 2) / 2


def octagon(side):
    return 2 * (1 + math.sqrt(2)) * side ** 2


def rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2


def trapezoid(base1, base2, height):
    return 0.5 * (base1 + base2) * height


