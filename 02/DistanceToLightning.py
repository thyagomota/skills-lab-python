# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that determines the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder (in seconds).

time = eval(input("Elapsed time? "))
distance = 1100 * time
print("Distance is %.2f ft or %.2f miles" % (distance, distance / 5280))
