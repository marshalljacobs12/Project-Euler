# Project Euler
# Problem 81: Path Sum: Two Ways
# Author: Marshall Jacobs

"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

                        [ 131 673 234 103 18  ]
                        [ 201 96  342 965 150 ]
                        [ 630 803 746 422 111 ]
                        [ 537 699 497 121 956 ]
                        [ 805 732 524 37  331 ]
 
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

import numpy as np
import time

start_time = time.time()

matrix = np.zeros((80, 80))

# read file into 80x80 array
with open('p081_matrix.txt', 'r') as f:
    counter = 0
    line = f.readline()
    while line:
        vals = line.strip('\n').split(',')
        for x in range(0, len(vals)):
            matrix[counter][x] = vals[x]
        line = f.readline()
        counter += 1

costMatrix = np.zeros((80, 80))

# Base case for DP
costMatrix[0][0] = matrix[0][0]

# left column base cases for DP
for i in range(1, len(matrix)):
    costMatrix[i][0] = costMatrix[i-1][0] + matrix[i][0]

# first row base cases for DP
for j in range(1, len(matrix[0])):
    costMatrix[0][j] = costMatrix[0][j-1] + matrix[0][j]

# max cost path DP moving only down and right
for m in range(1, len(matrix)):
    for n in range(1, len(matrix[0])):
        costMatrix[m][n] = min(
            costMatrix[m][n-1], costMatrix[m-1][n]) + matrix[m][n]

# Answer in costMatrix[79][79]
# Answer is max cost path through matrix moving only down and right
solution = costMatrix[len(matrix)-1][len(matrix[0])-1]
print('solution: ', solution)
# Outputs execution time (must be <1s)
print("--- %s seconds ---" % (time.time() - start_time))
