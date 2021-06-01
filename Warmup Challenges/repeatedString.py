#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

"""

There is a string, , of lowercase English letters that is repeated infinitely many times. Given an integer, , find and print the number of letter a's in the first  letters of the infinite string.


The substring we consider is abcacaabcac , the first 10 characters of the infinite string. There are 4  occurrences of a in the substring.
"""

def repeatedString(s, n):
    tam = len(s) - 1
    array = s
    i = 0
    
    if len(s) == 1:
        return n
    for j in range(0, n):
        if i <= tam:
            array+=(s[i])
            i+=1
        else:
            array+=(s[0])
            i=1
    print(array)
    return array.count('a')

    
if __name__ == '__main__':

    s = input('Introduce el string: ')

    n = int(input('Numero de caracteres a considerar: ').strip())

    result = repeatedString(s, n)

    print(result)