l = int(input())
nums = list(map(int,input().split()))

res = nums[0]
for i in range(1,l):
    if nums[i - 1] < nums[i]:
        diff = nums[i] - nums[i - 1]
        res += diff
    elif nums[i - 1] > nums[i]:
        diff =  nums[i - 1] - nums[i] 
        nums[i] += diff
    else:
        continue

print(res)