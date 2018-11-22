# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 88
# Question 1.2
# Solved by Yong Lin Wang

"""
    Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(str1, str2):
    ord1 = 0
    ord2 = 0
    for char in str1:
        ord1 += ord(char)
    for char in str2:
        ord2 += ord(char)

    return ord1 == ord2