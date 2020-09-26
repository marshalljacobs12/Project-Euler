# Project Euler
# Problem 6: Sum Square Difference
# Author: Marshall Jacobs

"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

from math import pow

# sum of squares
# Sn^2 = n(n+1)(2n+1)/6
sum100_squares = 100*(100+1)*(2*100+1)/6

# Gauss
sum100 = 50*101
sum100_2 = pow(sum100, 2)

solution = sum100_2 - sum100_squares

print(solution)
