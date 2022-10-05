import sys


length = int(input())
nums = list(map(int,input().split()))
nums.sort()
# print(nums)
left,right = 0,0
ans = -sys.maxsize
while right < length:
    while abs(nums[right] - nums[left]) > 5:
        ans = max(right - left,ans)
        left += 1
    right += 1
    ans = max(right - left,ans)

if ans == -sys.maxsize:
    print(length)
else:
    print(ans)
