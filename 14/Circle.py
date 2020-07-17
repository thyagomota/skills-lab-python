# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that finds the area and thecircumference of a circle given its radius.

import math

r = eval(input("r? "))
if r <= 0:
    print("r must be > 0")
else:
    area = math.pi * r**2
    circum = 2 * math.pi * r
    print("Area: %.2f, Circumference: %.2f" % (area, circum))
