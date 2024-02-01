import math

def cube(side):
    return 6 * side ** 2

def sphere(radius):
    return 4 * math.pi * radius **2

def cylinder(radius,height):
    return 2 * math.pi * radius ** 2 + (2 * math.pi * radius * height)

def cuboid(length, width, height):
    return 2 * (length * width + length * height + width * height)

def prism(base_area, height):
    return 2 * base_area + height * sum(base_area)


def cone(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    base_area = math.pi * radius**2
    lateral_area = math.pi * radius * slant_height
    return base_area + lateral_area

def pyramid(base_area, slant_height):
    base_perimeter = 4 * sum(base_area)
    lateral_area = 0.5 * base_perimeter * slant_height
    return sum(base_area) + lateral_area





