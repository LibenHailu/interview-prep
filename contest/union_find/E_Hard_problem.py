from functools import lru_cache
import sys


n = int(input())
cost = list(map(int,input().split()))
words = []
for _ in range(n):
    words.append(input())

@lru_cache()
def recur(i,c,s):
    # print(i,c,s)
    if i >= len(words):
        return c
    rev = str(words[i][::-1])
    if str(words[i]) < s and rev >= s:
        return min(recur(i+1,sys.maxsize,str(words[i])),recur(i+1,c+cost[i],rev))
    elif str(words[i]) >= s and str(rev) < s:
        return min(recur(i+1,c ,str(words[i])),recur(i+1,sys.maxsize,rev))
    elif str(words[i]) < s and rev < s:
        return -sys.maxsize
    else:
        return min(recur(i+1,c,str(words[i])),recur(i+1,c+cost[i],rev))
    
    # else:
    #     rev = words[i]
    
res = recur(0,0,"")
if res != -sys.maxsize:
    print(res)
else:
    print(-1)