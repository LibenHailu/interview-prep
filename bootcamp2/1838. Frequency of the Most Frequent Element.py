class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum_ = 0
        left = right = 0
        ans = 0
        while right < len(nums):
            sum_ += nums[right]
            while sum_ + k < (right - left + 1) * nums[right]:
                sum_ -= nums[left]
                left += 1
            ans = max(right-left+1,ans)
            right += 1
        
        return ans