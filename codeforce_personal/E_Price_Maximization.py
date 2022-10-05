
for _ in range(int(input())):
    l,k = map(int,input().split())
    nums = list(map(int,input().split()))
    left,right = 0,len(nums)-1
    ans = 0
    for i in range(l):
        ans += nums[i]//k
        nums[i] %= k
    nums.sort()
    while left < right:
        pair = nums[left] + nums[right]
        if  pair >= k:
            ans += 1
            left += 1
            right -= 1
        else:
            left += 1
    print(ans)