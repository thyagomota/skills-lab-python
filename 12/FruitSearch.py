# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that asks the user for the name of a fruit to search for. If the fruit is in the list (from the previous example), the program should say "fruit is available." Otherwise, the program should just print "fruit not found!"

fruits = ["orange", "strawberry", "blueberry", "banana"]
fruit = input("fruit? ")
if fruit in fruits:
    print("Fruit is available!")
else:
    print("Fruit not found!")
