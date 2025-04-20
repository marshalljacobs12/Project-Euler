# Project Euler
# Problem 1
# author: Marshall Jacobs

"""
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def isMultiple(x):
    if x % 3 == 0:
        return True
    elif x % 5 == 0:
        return True
    else:
        return False


def solve():
    threes = set(range(0, 1000, 3))
    fives = set(range(0, 1000, 5))
    return sum(threes.union(fives))


solution = solve()
print('solution: ', solution)
