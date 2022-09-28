# 1 2 2 5
# 1 2 5


length = int(input())
nums = list(map(int,input().split()))
# print(len(nums) - 2)
nums.sort()

print(max(0,len(nums)-nums.count(nums[0])-nums.count(nums[-1])))
