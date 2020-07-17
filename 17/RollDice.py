# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that simulates rolling a dice ten times. The program displays the probability of getting a 6.

import random
runs = 10000
n6   = 0
for _ in range(runs):
    roll = random.randrange(1, 7)
    print(roll, end = " ")
    if roll == 6:
        n6 += 1
print()
print("Probability of getting a 6 was %.2f%%" % (n6 / runs * 100))
