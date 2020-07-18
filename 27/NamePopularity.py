# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: File baby_names.csv contains the top 1,000 most popular names in U.S. in 2008
# Write a program that reads a name from the user and determines its popularity.

search = input("name? ")
found = False
f_in = open("baby_names.csv", "rt")
f_in.readline() # ignore the header line
for line in f_in:
    line = line.strip()
    year, name, percent, sex = line.split(",")
    name = name.replace("\"", "")
    if search == name:
        print("Percent:", percent)
        found = True
        break
f_in.close()
if not found:
    print(search, "couldn't be found!")