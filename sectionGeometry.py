"""
Write formula to calculate the section properties
"""
import math


def sectprop(sect_type, mat_type):
    if mat_type == 1:
        modulus = 35000
    else:
        modulus = 210000

    if sect_type == 1:
        print('What is the width and depth of the section?')
        width, depth = map(int, input().split())
        second_moment = width * depth ** 3 / 12
    else:
        print('What is the radius of the circular section [mm]?')
        radius = float(input())
        second_moment = math.pi / 4 * radius ** 4

    stiffness = modulus * second_moment

    return second_moment, stiffness
