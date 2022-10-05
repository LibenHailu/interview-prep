#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#

def twoStacks(maxSum, a, b):
    # Write your code here
    # return maxSum,a,b
    a = a[::-1]
    b = b[::-1]
    res = 0
    while a or b:
        # print(a,b,maxSum)
        if a and b and a[-1] < b[-1]:     
            if maxSum -a[-1] >= 0:
                res += 1
                maxSum -= a[-1]
                a.pop()
            else:
                break
        elif a and b and a[-1] > b[-1]:
            
            if maxSum -b[-1] >= 0:
                res += 1
                maxSum -= b[-1]
                b.pop()
            else:
                break
            
        elif a and not b:
            if maxSum -a[-1] >= 0:
                res += 1
                maxSum -= a[-1]
                a.pop()
            else:
                break
        elif b and not a:
            if maxSum -b[-1] >= 0:
                res += 1
                maxSum -= b[-1]
                b.pop()
            else:
                break
        # if maxSum >= 0:
        #     res += 1
        # else:
        #     break
    return res          
        

if __name__ == '__main__':
    print(twoStacks(10,[4, 2, 4, 6, 1],[2, 1, 8, 5]))
    print(twoStacks(10,[4],[2]))
    print(twoStacks(10,[4, 2, 4, 6, 1],[]))
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     g = int(input().strip())

#     for g_itr in range(g):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         maxSum = int(first_multiple_input[2])

#         a = list(map(int, input().rstrip().split()))

#         b = list(map(int, input().rstrip().split()))

#         result = twoStacks(maxSum, a, b)

#         fptr.write(str(result) + '\n')

#     fptr.close()
