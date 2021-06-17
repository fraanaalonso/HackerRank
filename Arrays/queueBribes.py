#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    moves = 0 
    q = [p-1 for p in q]
    for i,p in enumerate(q):
        if p - i > 2:
            print("Too chaotic")
            return
        for j in range(max(p-1,0),i):
            if q[j] > p:
                moves += 1
    print(moves)

if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q)
