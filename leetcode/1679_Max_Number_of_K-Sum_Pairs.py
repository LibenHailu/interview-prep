"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sums = 0
        nums.sort()
        i,j = 0,len(nums)-1
        while i < j:
            if nums[i] + nums[j] == k:
                sums += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i +=1
        return sums