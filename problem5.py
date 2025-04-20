# Project Euler
# Problem 5: Smallest Multiple
# Author: Marshall Jacobs

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without 
any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 
1 to 20?
"""

def smallest_multiple(n=20):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    multiple = 1
    for i in range(1, n + 1):
        multiple = lcm(multiple, i)
    
    return multiple

print(smallest_multiple())