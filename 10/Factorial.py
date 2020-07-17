# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that computes and displays the factorial of a given number. 

n = eval(input("n? "))
if n < 0:
    print("n must be nonnegative!")
else:
    factorial = 1
    for x in range(n, 0, -1):
        factorial = factorial * x
    print("%d! = %d" % (n, factorial))
