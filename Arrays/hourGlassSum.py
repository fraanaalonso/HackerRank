import math
import os
import random
import re
import sys

"""
There are  hourglasses in arr . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6 x 6
An hourglass in  arr is a subset A of values with indices falling in this pattern in 's graphical representation:
123
 2
234
"""

def hourglassSum(arr):
    toret = 0
    results = []
    for i in range(0, 4):
        for j in range(0, 4):
            toret = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) + (
                        arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
            results.append(toret)
    results.sort()
    return results.pop()



if __name__ == '__main__':

    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    max_Value = hourglassSum(arr)
    print(f'Max value is: {max_Value}')

