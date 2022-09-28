# find difference 
# calculate the cost
import enum
from sys import hash_info
from math import gcd

for _ in range(int(input())):
    n = int(input())
    t = input()
    hash_n = set([i + 1 for i in range(n)])
    hash_t = set()
    for i,b in enumerate(t):
        if b == "1":
            hash_t.add(i + 1)

    # print(hash_n)
    # print(hash_t)

    diff = list(hash_n - hash_t)
    # for i in range(len(diff)):
    #     for j in range(i+1,len(diff)):
    #         if gcd(diff[i],diff[j]) == diff[i]:
    #             diff[j] = diff[i]

    # print(diff)
    # print(sum(diff))    
    # diff.sort()
    # print(diff)
    # for val in diff:
    #     hash_n.remove(val)
    #     for hash
