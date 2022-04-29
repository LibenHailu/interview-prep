class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        for i, n in enumerate(nums):
            if n == 0:
                k -= 1

            if k < 0:
                if nums[l] == 0:
                    k += 1

                l += 1

        return len(nums) - l
