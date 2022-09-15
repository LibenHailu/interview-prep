from collections import defaultdict
tc = int(input())
for _ in range(tc):
    length = int(input()) - 1
    nums = list(map(int,input().split()))
    dp = defaultdict()
    for i in range(len(nums)-1,-1,-1):
        if length < (i + nums[i]):
            dp[i] = nums[i]
        else:
            dp[i] = nums[i] + dp[i + nums[i]]
    print(max(dp.values()))