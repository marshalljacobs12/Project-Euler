# Project Euler
# Problem 7: 10001st Prime
# Author: Marshall Jacobs

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
6th prime is 13.

What is the 10,001st prime number?
"""

def nth_prime(n):
    def is_prime(num):  
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    if n < 1:
        return None

    count = 0
    candidate = 1
    while count < n:
        candidate += 1
        if is_prime(candidate):
            count += 1
    return candidate

print(nth_prime(10001))