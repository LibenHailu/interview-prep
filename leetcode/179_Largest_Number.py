
""""
https://leetcode.com/problems/largest-number/
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str,nums))
        res = ""
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if int(str_nums[i]+str_nums[j]) < int(str_nums[j]+str_nums[i]):
                    str_nums[i],str_nums[j] = str_nums[j],str_nums[i]
    
        if len(str_nums) > 1:
            res  = "".join(str_nums).lstrip('0')
        else:    
            res = "".join(str_nums)         
    
        return res or '0'
    
