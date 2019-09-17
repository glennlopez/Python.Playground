import math
'''
https://www.youtube.com/watch?v=NE97ylAnrz4
'''


def sphere_vol(radius=-1):
    """
    Calculate the volume of a sphere
    :param radius: int or float
    :return: int or float
    """
    if radius < 0:
        print("Radius is missing.")
        return None
    return (4.0 / 3.0) * math.pi * radius ** 3


def triangle_area(b, h):
    '''
    Calculates area of a triangle
    :param b: base - float or int
    :param h: height - float or int
    :return: area - float or int
    '''
    return (1 / 2) * b * h


def cm(feet=0, inches=0):
    inch_cm = inches * 2.54
    feet_cm = feet * 12.0 * 2.54
    return feet_cm + inch_cm


print(sphere_vol(2))
print(triangle_area(3, 6))
print(cm(feet=5))
print(cm(feet=5, inches=11))
