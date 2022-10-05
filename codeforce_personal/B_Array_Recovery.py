for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    hasMany = False
    for i in range(1,len(nums)):
        if (-nums[i] + nums[i-1]) >= 0 and (nums[i] + nums[i-1]) >= 0 and (-nums[i] + nums[i-1]) != (nums[i] + nums[i-1]) :
            hasMany = True
        nums[i] = nums[i] + nums[i-1]
    
    if hasMany:
        print(-1)
    else:
        print(*nums)
