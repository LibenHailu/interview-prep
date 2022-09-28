# lets sort
# lets iterate through 3
# check all the condition
# have ans

import sys


for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    ans = sys.maxsize
    for i in range(length - 2):
        curr = nums[i:i+3]
        if curr[0] == curr[1] == curr[2]:
            ans = min(ans,0)
        if curr[0] == curr[1]:
            ans = min(ans,curr[2] - curr[1])
        if curr[1] == curr[2]:
            ans = min(ans,curr[1] - curr[0])
        if curr[0] != curr[1] != curr[2]:
            ans = min(ans,(curr[1] - curr[0] + curr[2] - curr[1]))
    
    print(ans)