#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


class Solution:
    def __init__(self, n):
        self.pars = [i for i in range(1, 2*n+1)]
        self.ranks = [1]*(2*n)


# def componentsInGraph(gb):
#     # Write your code here
#     # print(gb)
#     pars = [i for i in range(2*gb)]
#     ranks = [1]*(2*gb)

    def find(self, n1):
        if n1 != self.pars[n1 - 1]:
            n1 = self.pars[n1 - 1] = self.pars[self.pars[n1 - 1]]
            # return n1

        return n1

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)

        if r1 == r2:
            return False

        if self.ranks[r1] > self.ranks[r2]:
            self.pars[r2] = r1
            self.ranks[r1] += self.ranks[r2]
            self.ranks[r2] = 1
        elif self.ranks[r2] > self.ranks[r1]:
            self.pars[r1] = r2
            self.ranks[r2] += self.ranks[r1]
            self.ranks[r1] = 1
        else:
            self.pars[r2] = r1
            self.ranks[r1] += self.ranks[r2]
            self.ranks[r2] = 1
            # self.ranks[r1 - 1] += 1

    def countRes(self):
        print(self.ranks)
        mySet = set(self.ranks)
        mySet.remove(1)
        print(str(min(mySet))+" "+str(max(mySet)))
#         print(self.pars)
#         count = defaultdict(int)
#         for i in self.pars:
#             count[i] += 1

#         bigger = max(count.values() )
#         count = sorted(count.items(), key=lambda kv: kv[1])
#         smaller = 0
#         for i in count:
#             if i[1] > 1:
#                 smaller = i[1]
#                 break

#         print(str(smaller)+" "+str(bigger))


if __name__ == '__main__':
    #     fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #     n = int(input().strip())

    #     gb = []

    #     for _ in range(n):
    #         gb.append(list(map(int, input().rstrip().split())))

    #     result = componentsInGraph(gb)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    #     fptr.close()
    n = input()
    m = Solution(int(n))
    for i in range(int(n)):
        minp = list(map(int, input().split()))
        print(minp)
        m.union(minp[0], minp[1])
    m.countRes()
