n, enemy = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
left,right = 0,n - 1
res = 0
while left <= right:
    needed = 0
    p = enemy/nums[right]
    needed = int(p) + 1
    if ((right - left) + 1) >= needed:
        res += 1
    right -= 1
    left += needed - 1
print(res)
