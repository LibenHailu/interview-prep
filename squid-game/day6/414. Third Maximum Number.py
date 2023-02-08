class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 1
        curr = nums[0]
        for num in nums:
            if num != curr:
                curr = num
                count += 1
            if count == 3:
                return curr
        
        return nums[0]
