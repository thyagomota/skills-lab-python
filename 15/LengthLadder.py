# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program to determine the length of a ladder required to reach a given height when leaned against a wall at a certain degree angle.

import math
height = eval(input("height? "))
if height <= 0:
    print("height must be > 0")
else:
    angle_degrees = eval(input("angle? "))
    angle_radians = math.pi / 180 * angle_degrees
    # or you can use the radians function available in math
    # angle_radians = math.radians(angle_degrees)
    length = height / math.sin(angle_radians)
    print("Length of ladder: %.2f" % length)
