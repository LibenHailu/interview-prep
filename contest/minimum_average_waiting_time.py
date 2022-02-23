#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#


def minimumAverage(customers):
    # Write your code here
    h = []
    for order in customers:
        heapq.heappush(h, [order[1], order[0]])

    l = []
    while h:
        time, arrival = heapq.heappop(h)
        if not l:
            l.append(time + arrival - 0)
        l.append(l[len(l) - 1] + time + arrival - 0)

    sum = sum(l)

    return sum//len(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
