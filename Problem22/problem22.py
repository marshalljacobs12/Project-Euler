# Project Euler
# Problem 22: Name Scores
# Author: Marshall Jacobs

"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
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

score = 0

# read in words and populate points dictionary
with open('p022_names.txt', 'r') as f:
    words_str = f.read()
    words = [x.strip('"') for x in words_str.split(',')]
    words.sort()
    for i in range(len(words)):
        wordScore = 0
        # calculate word value
        for c in words[i]:
            wordScore += letterVal[c]
        # multiply word value by position and add to score
        score += (i+1)*wordScore

# Outputs the total of all name scores
print('score: ', score)
# Outputs execution time (must be <1s)
print("--- %s seconds ---" % (time.time() - start_time))
