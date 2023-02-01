for _  in range(int(input())):
    l = int(input())
    nums = list(map(int,input().split()))
    max_ = max(nums)
    min_ = min(nums)
    for num in nums:
        max_ = max(max_,max_ | num)
        min_ = min(min_,min_  & num)
    print(max_ - min_)
