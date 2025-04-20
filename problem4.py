# Project Euler
# Problem 4: Largest Palindrom Product
# Author: Marshall Jacobs

"""
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def largest_palindrome_product():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):  # Start j from i to avoid duplicate pairs
            product = i * j
            if str(product) == str(product)[::-1]:  # Check if product is a palindrome
                max_palindrome = max(max_palindrome, product)
    return max_palindrome

print(largest_palindrome_product())