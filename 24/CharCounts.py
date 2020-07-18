# MSU Denver - Skills Lab - Summer 2020
# Instructor: Thyago Mota
# Description: Reads a string and displays its number of vowels, consonants, and digits​

text = input('Enter a string: ')
text = text.lower()
vowels = consonants = digits = 0
for c in text:
    if c in '0123456789':
        digits += 1
    elif c in 'abcdefghijklmnopqrstuvwxyz':
        if c in 'aeiou':
            vowels += 1
        else:
            consonants += 1
print(text, 'has', vowels, 'vowels,', consonants, 'consonants, and', digits, 'digits')

