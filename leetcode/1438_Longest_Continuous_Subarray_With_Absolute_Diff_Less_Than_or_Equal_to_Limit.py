class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_ = collections.deque()
        min_ = collections.deque()
        l = 0
        max_len = 0

        for r in range(len(nums)):
            while max_ and max_[-1] < nums[r]:
                max_.pop()
            max_.append(nums[r])
            while min_ and min_[-1] > nums[r]:
                min_.pop()
            min_.append(nums[r])
            while l <= r and max_ and min_ and max_[0] - min_[0] > limit:
                if max_[0] == nums[l]:
                    max_.popleft()
                if min_[0] == nums[l]:
                    min_.popleft()
                l += 1    
            max_len = max(max_len, r - l + 1)    
        
        return max_len  