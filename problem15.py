# Project Euler
# Problem 15: Lattice paths
# Author: Marshall Jacobs

"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right 
and down, there are exactly routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
"""
from math import factorial

def lattice_paths(n):
    # The number of lattice paths in an n x n grid is given by the binomial coefficient C(2n, n)
    # which is (2n)! / (n! * n!)
    return factorial(2 * n) // (factorial(n) * factorial(n))

print(lattice_paths(20))  # Output: 137846528820