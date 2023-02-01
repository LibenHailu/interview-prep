import math
import sys


for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    mn,mx = 0, sys.maxsize
    for i in range(len(nums) - 1):
        x = nums[i]
        y = nums[i + 1]
        if x < y:
            mx = min(mx,(x + y ) // 2)
        elif x > y:
            mn = max(mn,(x + y + 1) // 2)
    if mn <= mx:
        print(mn)
    else:
        print(-1)
    # s = sorted(nums)
    # sr = sorted(nums,reverse=True)
    # h = set(nums)

    # if nums == s:
    #     print(0)
    #     continue
    # elif nums == sr:
    #     print(max(nums))
    #     continue
    # elif len(h) == 2:
    #     hl = list(h)
    #     mx,mn = max(hl),min(hl)

    # nums.sort()
    # nums = []
    # for num in numsx:
    #     nums.append(num)
    # # print(sum(nums)//len(nums))
    # for i,num in enumerate(nums):
    #     nums[i] = abs(num - 40741153)

    # print(nums)
    # print(numsx)
    # numsx.sort()
    # print(numsx)