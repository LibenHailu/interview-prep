class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
                fast += 1
