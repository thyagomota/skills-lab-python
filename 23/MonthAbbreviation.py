# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: Prints the abbreviation of the month that corresponds to a given month number​

month = eval(input('month? '))
months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
index = (month - 1) * 3
print(months[index:index + 3])

