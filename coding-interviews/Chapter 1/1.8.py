# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 91
# Question 1.8 - Zero Matrix
# Solved by Yong Lin Wang

"""
    Approach 1
    Complexity: 
        Define n: n being the number of elements in the longest row
        Average: O(n^2)
        Best: O(n^2)
        Worst: O(n^3)
"""

matrix = [
    [1,2,3],
    [12,9,6],
    [7,8,0]
]

def zeroify(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                for k in range(len(matrix[i])):
                    matrix[i][k] = 0
                for k in range(len(matrix)):
                    matrix[k][j] = 0


zeroify(matrix)
print(matrix)
