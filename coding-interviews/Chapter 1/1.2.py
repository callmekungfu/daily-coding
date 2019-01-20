# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 88
# Question 1.2
# Solved by Yong Lin Wang

"""
    Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(str1, str2):
    """
        If two strings are permutation to one another, they should have the same
        characters. This solution evaluates the sum of the orders of the strings
        if they are the same then they are permutation to one another, otherwise,
        they are not and I am a fucking retard that cant get any shit done properly
        i am such a failure in life that I cant do anything right. :(
    """
    ord1 = 0
    ord2 = 0
    for char in str1:
        ord1 += ord(char)
    for char in str2:
        ord2 += ord(char)

    return ord1 == ord2