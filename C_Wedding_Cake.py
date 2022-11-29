from collections import Counter, defaultdict
import sys


l = int(input())
nums = list(map(int,input().split()))
# count = Counter(nums)
count = defaultdict(int)
for num in nums:
    if num == 1:
        count[1] += 1
    # else:
    elif num - 1 in count and count[num - 1] > count[num]:
        count[num] += 1
    
    # if num <= len(count) or num == len(count) + 1:
    #     count[num] = 1 + count.get(0,num)
# print(count )
res = sys.maxsize
for i in range(1,6):
    res = min(res,count[i])
if res != sys.maxsize:
    print(res)
else:
    print(0)
