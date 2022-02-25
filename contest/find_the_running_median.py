#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import heappush, heappop

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#


def runningMedian(a):
    # Write your code here
    min_h = []
    max_h = []
    res = []
    for num in a:
        if not min_h:
            heappush(min_h, num)

        elif len(min_h) > len(max_h):
            cur_mid = min_h[0]
            if num > cur_mid:
                heappush(max_h, -heappop(min_h))
                heappush(min_h, num)
            else:
                heappush(max_h, -num)

        elif len(min_h) == len(max_h):
            cur_mid = min_h[0]
            if num > cur_mid:
                heappush(min_h, num)
            else:
                heappush(max_h, -num)
        else:
            cur_mid = -max_h[0]
            if num < cur_mid:
                heappush(min_h, -heappop(max_h))
                heappush(max_h, -num)
            else:
                heappush(min_h, num)

        if len(min_h) > len(max_h):
            res.append(min_h[0])

        elif len(min_h) < len(max_h):
            res.append(-max_h[0])

        else:
            res.append((min_h[0] + -max_h[0]) / 2)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)
    print(result)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
