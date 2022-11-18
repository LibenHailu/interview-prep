from functools import lru_cache
import sys


n,a,b,c=map(int,input().split())
# z=[0]+[-1e9]*5000
# for i in range(1,n+1):z[i]=max(z[i-a],z[i-b],z[i-c])+1
# print(z[n])
nums = [a,b,c]

# memo = [-sys.maxsize] * (n + 1)
# def curRibbon(n):
#     if n <= 0:
#         return 0
#     if memo[n] != -sys.maxsize:
#         return memo[n]

#     q = -sys.maxsize
#     for num in nums:
#         if n - num >= 0:
#             q = max(q,1 + curRibbon(n - num))
#     memo[n] = q
#     return memo[n]

# print(curRibbon(n))
memo = [0] * (n + 1)
best = []
def curRibbon(n):
    # if n <= 0:
    #     return 0
    # if memo[n] != -sys.maxsize:
    #     return memo[n]

    for i in range(1,n ):
        q = -sys.maxsize
        # best = []
        for num in nums:
            if i - num >= 0 and 1 + memo[i - num] > q:
                q = max(q,1 + memo[i - num])
                best.append(num)
                print(best)
        memo[i] = q
    return memo[n]
print(best)
print(curRibbon(n))
