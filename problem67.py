# Project Euler
# Problem 67
# Author: Marshall Jacobs

"""
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

               3
              7 4
             2 4 6
            8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save 
Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (1012) routes every second it would take over twenty billion 
years to check them all. There is an efficient algorithm to solve it. ;o)
"""
import time
import numpy as np

start_time = time.time()

triangleMatrix = np.zeros((100, 100))

with open('p067_triangle.txt', 'r') as f:
    line = f.readline()
    counter = 0
    while line:
        vals = line.strip('\n').split(' ')
        for x in range(0, len(vals)):
            triangleMatrix[counter][x] = vals[x]
        line = f.readline()
        counter += 1

costMatrix = np.array([[0]*100]*100)

# Base case for DP
costMatrix[0][0] = triangleMatrix[0][0]

# left column base cases for DP
for i in range(1, len(triangleMatrix)):
    costMatrix[i][0] = costMatrix[i-1][0] + triangleMatrix[i][0]

# first row base cases for DP
for j in range(1, len(triangleMatrix[0])):
    costMatrix[0][j] = costMatrix[0][j-1] + triangleMatrix[0][j]

# max cost path DP
for m in range(1, len(triangleMatrix)):
    for n in range(1, len(triangleMatrix[0])):
        costMatrix[m][n] = max(
            costMatrix[m-1][n-1], costMatrix[m-1][n]) + triangleMatrix[m][n]

maxSum = max(costMatrix[len(triangleMatrix)-1])

# Outputs the max-cost path through the triangle
print('maxsum: ', maxSum)
# Outputs execution time (must be <1s)
print("--- %s seconds ---" % (time.time() - start_time))
