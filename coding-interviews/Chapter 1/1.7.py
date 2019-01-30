# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 91
# Question 1.7 - Rotate Matrix
# Solved by Yong Lin Wang

import unittest
import copy

image = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

result = [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

"""
    Approach 1
    Complexity: 
        Average: O(n^2), n = number of characters in the original string
        Best: O(1), n = number of characters in the original string
        Worst: O(n^2), n = number of characters in the original string
"""

def rotate_matrix(img):
    new_image = []
    for i in range(len(img)):
        new_image.append(img[i].copy())
    for i in range(len(img)):
        count = 0 
        for j in range(len(img)-1,-1,-1):
            new_image[i][count] = img[j][i]
            count += 1
    return new_image

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate_matrix(image), result)
        print("Test Completed Successfully")

MyTest().test()