# file with the functions for the code

import os
import math

# basic operations

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "e"
    return a / b

def pow(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "e"
    return math.sqrt(a)

# formula operations

def area_circle(radius):
    return math.pi * radius ** 2

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def quadratic_formula(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "e"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2
    
def pitagorean_theorem(a, b):
    return math.sqrt(a ** 2 + b ** 2)

# other functions

def cls():
    os.system("cls")
