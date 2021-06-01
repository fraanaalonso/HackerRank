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
    c = 1
    count = 0
    for value in q:
        if (value - c) == 2:
            count+=2
        elif (value - c) == 1:
            count += 1
        elif (value - c) > 2:
            print('Too chaotic')
            return
        c+=1
    print(count)

if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q)
