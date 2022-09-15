# have a recursive function
# save the index of the min and max points
# your states are i,j,step
# take the min of steps
from functools import lru_cache
import sys
for _ in range(int(input())):
    length = int(input())
    nums = list(map(int,input().split()))
    max_ = nums.index(max(nums))
    min_ = nums.index(min(nums))
    @lru_cache(maxsize=None)
    def rec(i,j,count):
        print(i,j,count)
        if i > max_ and i > min_ or  j < max_ and j < min_ or i > min_ and j < max_:
            
            return count
        # if i > j or 0 <= i < length or 0 <= j < length:
        #     return sys.maxsize
        
        return min(rec(i+1,j,count + 1),rec(i,j-1,count + 1))
    
    print(rec(0,length-1,0))