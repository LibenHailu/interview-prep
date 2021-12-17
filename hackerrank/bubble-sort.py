#!/bin/python3

import math
import os
import random
import re
import sys

"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""


def countSwaps(a):
    countSwap = 0
    # Write your code here
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                countSwap = countSwap + 1
    print("Array is sorted in {} swaps.".format(countSwap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
