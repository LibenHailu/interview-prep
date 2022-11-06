import math


for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    res = nums[0]
    for i in range(1,l):
        res &= nums[i]
    
    print(res)