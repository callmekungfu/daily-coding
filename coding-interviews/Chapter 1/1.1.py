# Cracking the Coding Interview 6th Edition
# Chapter 1 - Arrays and Strings. Page 88
# Question 1.1
# Solved by Yong Lin Wang

"""
    Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
""" 

def is_unique_sets(s):
    """
        The most straightforward approach in python is to utilize the power of sets.
        Sets are implementations of hash table that allows fast read/write operations
        In this case we will split the string into a list then convert into
    """
    s_splitted = s.split()
    return len(s_splitted) == len(set(s_splitted))

def is_unique_sorted(s):
    """
        Without using any additional data structures, it is difficult to achieve the best
        time complexity. However, by simply using sorting, the time complexity of the
        algorithm can be reduced to O(nlogn)

        This function utilizes the sorting approach to solving this problem.

        Time Complexity: O(nlogn)
    """

    sorted_s = sorted(s)
    for i in range(0, len(sorted_s) - 1):
        if sorted_s[0] == sorted_s[i+1]:
            return False
    return True