# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that asks the user for a temperature in Fahrenheit. If the temperature is greater than 90F, the program prints a heat warning. Else, if the temperature is less than 30F, the program prints a cold warning.

fahrenheit = eval(input("Fahrenheit? "))
if fahrenheit > 90:
    print("Heat warning!")
elif fahrenheit < 40:
    print("Cold warning!")
else:
    print("Nice weather!")
