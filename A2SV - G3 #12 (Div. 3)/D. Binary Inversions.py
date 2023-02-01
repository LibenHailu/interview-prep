def findMax(nums):
    ones = 0
    res = 0
    for i,v in enumerate(reversed(nums)):
        if v == 1:
            res += len(nums) - (len(nums) - (i)) - ones
            ones += 1
    
    return res

for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    # ans = 0
    ans = findMax(nums)
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 1
            ans = max(ans,findMax(nums))
            nums[i] = 0
            break
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 1:
            nums[i] = 0
            ans = max(ans,findMax(nums))
            nums[i] = 1
            break
    
    print(ans)
        

