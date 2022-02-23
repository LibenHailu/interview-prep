#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def runningMedian(a):
    print(a)
    # Write your code here
    l = a.sort()
    if len(l) % 2 == 0:
        return format(l[len(l)//2], '.1f')
    index = len(l)//2
    sum = l[index] + l[index + 1]
    average = sum/2
    return format(average, '.1f')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
