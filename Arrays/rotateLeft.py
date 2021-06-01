import math
import os
import random
import re
import sys
from collections import deque
# This is a sample Python script.

"""

A left rotation operation on an array shifts each of the array's elements 1  unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3, 4, 5, 1, 2]. Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array a of n integers and a number d, d, perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

"""
def rotLeft(a, d):
    arr = deque(a)
    arr.rotate(-d)
    arr = list(arr)

    return arr
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [1,2,3,4,5]
    result = rotLeft(array, 2)

    print(f'Array: {result}')