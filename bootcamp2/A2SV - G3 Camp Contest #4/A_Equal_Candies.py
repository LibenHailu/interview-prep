for _ in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    min_ = min(nums)
    res = 0
    for num in nums:
        res += num - min_
    
    print(res)