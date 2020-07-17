# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that finds the roots of a quadratic equation given its coefficients "a," "b," and "c."

import math
a = eval(input("a? "))
b = eval(input("b? "))
c = eval(input("c? "))
if a == 0:
    print("No roots!")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("No roots!")
    else:
        print(delta)
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 * a
        print("x1 = %.2f" % x1)
        print("x2 = %.2f" % x2)
