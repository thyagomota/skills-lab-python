# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: A program that reads a string and generates a new string by removing the vowels of the original string​, preserving case.

text = input('Enter a string: ')
new_text = ''
for c in text:
    if c not in 'aeiouAEIOU':
        new_text += c
print(new_text)

