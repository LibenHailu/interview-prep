from functools import lru_cache


n = int(input())
boys = list(map(int,input().split()))
m = int(input())
girls = list(map(int,input().split()))
boys.sort()
girls.sort()
@lru_cache(None)
def dp(i,j):
    if i >= n  or j >= m:
        return 0
    if boys[i] == girls[j] or boys[i] == girls[j] + 1 or boys[i] + 1 == girls[j]:
        return 1 + dp(i + 1, j + 1) 
    else:
        return max(dp(i + 1, j),dp(i, j + 1)  )

print(dp(0,0))