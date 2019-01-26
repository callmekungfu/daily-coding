# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 91
# Question 1.5 One Away
# Solved by Yong Lin Wang

"""
    There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away. 
"""

def one_edit_away(a,b):
    # Insert Character Check
    if len(a) > len(b):
        longer = list(a)
        shorter = list(b)
    else:
        longer = list(b)
        shorter = list(a)
    
    count = 0

    for char in shorter:
        if char in longer:
            count += 1

    if count == len(shorter): 
        return True
    elif (count == len(shorter) - 1) and (len(shorter) == len(longer)):
        return True

    return False

while True:
    print(str(one_edit_away(input('a: '), input('b: '))))