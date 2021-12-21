"""
https://leetcode.com/problems/arithmetic-subarrays/submissions/
"""
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arithmatic_bool = []
        for i in range(len(r)):
            sub_arr = nums[l[i]:r[i]+1]
            sub_arr.sort()
            is_art = True
            for j in range(2,len(sub_arr)):
                if len(sub_arr) != 2 and sub_arr[j] - sub_arr[j-1] != sub_arr[1] - sub_arr[0]:
                        is_art = False
                        break
            arithmatic_bool.append(is_art)
                
        return arithmatic_bool