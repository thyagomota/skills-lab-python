# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: Write a program that allows a teacher to enter and save students' names and grades.
# The program should save the students in a CSV file.

f_out = open("students.csv", "wt")
print("Enter the student names and grades (hit ENTER when you are done!")
while True:
    name = input("name? ")
    name = name.strip()
    if len(name) == 0:
        break
    grade = eval(input("grade? "))
    f_out.write(name + "," + str(grade) + "\n")
f_out.close()
print("done!")

