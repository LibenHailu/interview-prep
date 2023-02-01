# from collections import defaultdict
# import heapq
# import sys


for _ in range(int(input())):
    n,m = map(int,input().split())
    ans = 0
    if n == 1:
        print(sum(i for i in range(1,m+1)))
        continue
    if m == 1:
        print(sum(i for i in range(1,n+1)))
        continue
    ans = 0
    for x in range(1,m):
        ans += x
    for x in range(1,n + 1):
        ans += (x - 1)*m  + m
    print(ans)
