from audioop import mul


length, k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
multiple = set()
for i in range(len(nums)-1,-1,-1):
    if  nums[i] * k not in multiple:
        multiple.add(nums[i])    
print(len(multiple))

