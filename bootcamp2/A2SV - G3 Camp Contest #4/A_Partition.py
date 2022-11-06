l = int(input())
nums = list(map(int,input().split()))
res = 0
for i in range(l):
    if nums[i] >= 0:
        res += nums[i]
    else:
        res += -nums[i]

print(res)