# sicnce we care about pairs 
# create a dp array
# start form len - 2
# as long as long as the sum is not satisfied keep moving on
# when you got dp + 1
# subtract max form len and r eturn that
 
tc  = int(input())
for _ in range(tc):
    length = int(input())
    dp = [0]* 5 
    nums = list(map(int,input().split()))
    if length == 2:
        print(0)
        continue
    for i in range(len(nums) - 2 , - 1,-1):
        r = i + 1
        while r < len(nums) and  (nums[i] + nums[r]) % 2 != 0:
            r += 1
        
        if r == len(nums) - 1:
            dp[i] = 2
        elif r < len(nums):
            dp[i] = 1 + dp[r]
    
    print(length - max(dp))