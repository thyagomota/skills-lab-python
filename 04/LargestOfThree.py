# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that asks the user to enter three numbers. The program should then display the largest of the three numbers entered by the user.

a = eval(input("a? "))
b = eval(input("b? "))
c = eval(input("c? "))
if a >= b and a >= c:
    print("%d is the largest!" % (a))
elif b >= a and b >= c:
    print("%d is the largest!" % (b))
else:
    print("%d is the largest!" % (c))
