#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    # Write your code here

    h = A
    counter = 0

    heapq.heapify(h)

    if h[0] >= k:
        print(-1)

    while h[0] < k:
        print("i am here")
        counter += 1

        first_value = heapq.heappop(h)
        second_value = heapq.heappop(h)

        sum = first_value + 2 * second_value
        heapq.heappush(h, sum)

    print(counter)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # A = list(map(int, input().rstrip().split()))

    # result = cookies(k, A)

    # fptr.write(str(result) + '\n')

    # fptr.close()
    print(cookies(7,
                  [1, 2, 3, 9, 10, 12]))
