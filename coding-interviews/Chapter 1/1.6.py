# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 91
# Question 1.6 String Compression
# Solved by Yong Lin Wang

import unittest
import random

"""
    Approach 1
    Complexity: 
        Average: O(n), n = number of characters in the original string
        Best: O(n), n = number of characters in the original string
        Worst: O(n), n = number of characters in the original string
"""

def compress_string(original):
    string_mapped = {}
    new_string = original[0]
    counter = 1
    for i in range(1, len(original)):
        if original[i] == new_string[-1]:
            counter += 1
        else:
            new_string = new_string + str(counter) + original[i]
            counter = 1
    new_string += str(counter)
    if len(new_string) >= len(original):
        return original
    return new_string

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
        print("Test Completed with " + str(NUM_OF_TESTS) + " attempts.")

        
        

MyTest().test()