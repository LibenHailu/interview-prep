class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        # nums[0] = nums[0] + k
        # nums[-1] = nums[-1] - k
        result = nums[-1] - nums[0]

        for j in range(1, len(nums)):
            cur_max = max(nums[len(nums)-1] - k, nums[j-1] + k)
            cur_min = min(nums[0] + k, nums[j] - k)
            result = min(result, cur_max - cur_min)

        return result
