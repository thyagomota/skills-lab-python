# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that implements a simple guessing game: it randomly generates a number (between 1 and 100) so the user can try to guess it. The program should give hints like the number is less or greater than the user choice. 

import random
guess = random.randrange(1, 101)
found = False
while not found:
    choice = eval(input("? "))
    if choice == guess:
        found = True
    elif guess < choice:
        print("The number is lower")
    else:
        print("The number is higher")
print("You guessed right!")
