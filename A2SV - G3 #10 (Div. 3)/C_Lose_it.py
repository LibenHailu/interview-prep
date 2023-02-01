from collections import defaultdict


l = int(input())
nums = list(map(int,input().split()))
# n = { 4,8,15,16,23,42}
prerequisite = {8:4,15:8,16:15,23:16,42:23}
d = defaultdict(int)
for num in nums:
    if num == 4:
        d[num] += 1
    elif d[prerequisite[num]] != 0 :
        d[prerequisite[num]] -= 1
        d[num] += 1
print(len(nums) - d[42] * 6)

