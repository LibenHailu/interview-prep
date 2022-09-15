
# accept the input as nums list
#  use counter to count frequency
# iterate over the nums
# if it has freq over 1 update it by 1
# change to set 
# return len of the set
from typing import Counter


tc = int(input())
for _ in range(tc):
    input()
    nums = list(map(int,input().split()))
    count = Counter(nums)
    for i in range(len(nums)):
        if count[nums[i]] > 1:            
            count[nums[i]] -= 1
            nums[i] += 1
    
    print(len(set(nums)))