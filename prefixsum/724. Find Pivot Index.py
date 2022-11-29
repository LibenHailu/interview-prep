class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        prefix.append(0)
        for i in range(1,len(nums) + 1):
            if prefix[i - 1] - prefix[0] == prefix[len(nums)] - prefix[i]:
                return i - 1
        
        return -1
        