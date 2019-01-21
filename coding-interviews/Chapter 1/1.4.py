# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 88
# Question 1.4 Palindrome Permutations
# Solved by Yong Lin Wang

"""
    Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
"""

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
    
    characters = text.split('')
    

print(palindrome_detector(input("Your Text: ").strip()))
