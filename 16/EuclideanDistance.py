# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that reads two points in a plane (x1,y1) and (x2,y2) and determines the Euclidean distance between them.

import math
x1 = eval(input("x1? "))
y1 = eval(input("y1? "))
x2 = eval(input("x2? "))
y2 = eval(input("y2? "))
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance = %.2f" % d)
