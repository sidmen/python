import string
import random
# print(help(string))
# print(string.ascii_letters)
# print(string.ascii_lowercase)
#
# print(random.choice('pull a letter from here'))
# print(random.choice(string.ascii_lowercase))


def generator():
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3+letter4+letter5
    return(name)


print(generator())

letter_input1 = input(
    'Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input2 = input(
    'Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input3 = input(
    'Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input4 = input(
    'Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')
letter_input5 = input(
    'Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter')


vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letter = string.ascii_lowercase
