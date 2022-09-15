# find longest common sub seq
# and substract it form the longer string
# pritn the res
# use lru 
from functools import lru_cache
# import re

s1 = input()
s2 = input()
res = 0
@lru_cache(maxsize=None)
def dp(i,j,count):
    global res
    if s1[i] == s2[j] and i == j:
        count += 1
        res = max(res, count)
    if 0 <= i < len(s1) - 1 and 0 <= j < len(s2) - 1:
        dp(i + 1,j,count)
        dp(i ,j + 1,count)
dp(0,0,0)

if res == max(len(s1),len(s2)):
    print(-1)
else:
    print(max(len(s1),len(s2)) - res)
