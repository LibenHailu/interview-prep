l,k = map(int,input().split())
nums = list(map(int,input().split()))
cur_sum = 0
for j in range(k):
    cur_sum += nums[j]

res,ind = cur_sum,1

for i in range(k,len(nums)):
    cur_sum += nums[i]
    cur_sum -= nums[i - k]
    if cur_sum < res:
        res,ind = cur_sum,i - k + 2

print(ind)