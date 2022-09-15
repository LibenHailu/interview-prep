# make xor of each sub sequence
# take the greatest
import sys


length = int(input())
nums = list(map(int,input().split()))
ans = -sys.maxsize
for i in range(length):
    cur_xor = 0
    for j in range(i,length):
        cur_xor = cur_xor ^ nums[j]
        ans = max(ans,cur_xor)
    
if ans != -sys.maxsize:
    print(ans)