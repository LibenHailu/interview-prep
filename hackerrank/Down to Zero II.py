#!/bin/python3

from collections import deque
import math
import os
import random
import re
import sys


#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Write your code here
    count = 0
    queue = deque([(n,count)])
    memo = set()
    while queue: 
        n,count = queue.popleft()
        if n < 1:
            if n == 1:
                count += 1
            break
        if n - 1 not in memo:
            memo.add(n-1)
            queue.append((n-1,count+1))
            
        for i in range(int(math.sqrt(n)),1,-1):
            factor = max(n//i,i)
            if n % i == 0 and factor not in memo:
                memo.add(factor)
                queue.append((factor,count+1))
        

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
