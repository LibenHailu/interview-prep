class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)   
        left,right  = 0, len(nums)-1
        index = len(nums) - 1
        while left <=right:          
            if nums[left] * nums[left]  > nums[right] * nums[right]:
                res[index] = nums[left] * nums[left]
                index -= 1
                left += 1
            else:
                res[index] = nums[right] * nums[right]
                index -= 1
                right -= 1
        
        return res