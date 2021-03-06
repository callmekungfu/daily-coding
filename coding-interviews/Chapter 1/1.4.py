# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 88
# Question 1.4 Palindrome Permutations
# Solved by Yong Lin Wang

"""
    Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
"""

from random import shuffle

def palindrome_detector(text):
    string_map = {}
    text = text.replace(' ', '')
    for char in text:
        if char in string_map:
            string_map[char] += 1
        else:
            string_map[char] = 1
    single_flag = True
    for char in string_map:
        if(string_map[char] % 2 != 0):
            if(single_flag and (len(text) % 2 != 0)):
                single_flag = False
            else:
                return False
    return True

def palindrom_builder(text):
    if not palindrome_detector(text):
        raise ValueError("String Provided is Not Palindromable.")
    
    characters = list(text)
    space = characters.count(' ') > 0
    characters = list(filter((' ').__ne__, characters))

    single_char = ''

    for char in characters: 
        if characters.count(char) == 1:
            characters.remove(char)
            single_char = char
    
    shuffle(characters)
    length = len(characters) // 2

    buffer = ''

    while len(characters) > 0:
        buffer += characters[0]
        characters = list(filter((characters[0]).__ne__, characters))

    buffer_reversed = buffer[::-1]

    buffer += single_char
    if space:
        buffer += ' '
    buffer += buffer_reversed
    
    return buffer
    
target = input("Your Text: ").strip()

print(str(palindrome_detector(target)) + ',', 'Examples:', palindrom_builder(target) + ',', palindrom_builder(target), 'and more.')



