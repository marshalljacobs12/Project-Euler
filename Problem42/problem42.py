# Project Euler
# Problem 42: Coded Triangle Numbers
# Author: Marshall Jacobs

"""
The nth term of the sequence of triangle numbers is given by, tn = 1/2*n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using p042_words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import time

start_time = time.time()

# Letter Scores
letterVal = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

# points has a key that is a word value and a value that is a list of words with that word value
points = {}
# read in words and populate points dictionary
with open('p042_words.txt', 'r') as f:
    g = f.read()
    g1 = [x.strip('"') for x in g.split(',')]
    maxScore = 0
    for x in g1:
        wordScore = 0
        # calculate word value for a single word
        for c in x:
            wordScore += letterVal[c]
        if wordScore > maxScore:
            maxScore = wordScore
        if wordScore in points:
            points[wordScore].append(x)
        else:
            points[wordScore] = [x]

# Get triangle number candidates for words (Only need triangle numbers < maxScore)
triangleNumbers = []
t_n = 1
triangleNumbers.append(t_n)
n = 2
while(True):
    t_n = 0.5*n*(n+1)
    if t_n > maxScore:
        break
    triangleNumbers.append(t_n)
    n += 1

# create a list of all words that have word values equal to triangle numbers
words = []
for i in triangleNumbers:
    if i in points:
        words.extend(points[i])

# Outputs # words with triangle number word values
print(len(words))
# Outputs execution time (must be <1s)
print("--- %s seconds ---" % (time.time() - start_time))
