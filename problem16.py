# Project Euler
# Problem 16: Power Digit Sum
# Author: Marshall Jacobs

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
def power_digit_sum(base=2, exponent=1000):
    number = base ** exponent
    return sum(int(digit) for digit in str(number))

print(power_digit_sum())