# simple binary search
length, power = map(int,input().split())
nums = sorted(list(map(int,input().split())))
left,right = 0,length - 1
res = 0

while left <= right:
    needed = 0
    p = power/nums[right]
    needed = int(p) + 1
    if ((right - left) + 1) >= needed:
        res += 1
    right -= 1
    left += needed - 1
print(res)
