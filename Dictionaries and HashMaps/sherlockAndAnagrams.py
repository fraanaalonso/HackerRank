import math
from collections import defaultdict


def sherlockAndAnagrams1(s):
    array = list(s)
    count = 0

    for ancho in range(1, len(array) - 1):
        if ancho == 1:
            for i in range(0, len(array) - 1):
                for j in range(i + 1, len(array)):
                    if array[i] == array[j]:
                        count += 1
        else:
            if ancho != len(array):
                for i in range(ancho, len(array)):
                    for j in range(1, len(array)):
                        x = array[:i]
                        y = array[j:j + i]
                        if sorted(x) == sorted(y):
                            count += 1

    return count

def sherlockAndAnagrams(s):
    d = defaultdict(int) # to avoid key error
    ans = 0
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            d[''.join(sorted(s[j:j + i]))] += 1
            print(d)

    for key, value in d.items():
        ans += value * (value - 1) // 2

    return ans
if __name__ == '__main__':
    done = sherlockAndAnagrams('abba')
    print('Answer: ', done)