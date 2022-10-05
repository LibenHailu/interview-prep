class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        L,M = firstLen,secondLen
        if len(nums) < L + M: 
            return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, maxL, maxM = nums[L + M - 1], nums[L - 1],nums[M - 1]
        for i in range(L + M, len(nums)):
            maxL = max(maxL, nums[i - M] - nums[i - M - L])
            maxM = max(maxM, nums[i - L] - nums[i - L - M])
            res = max(res, maxL + nums[i] - nums[i - M], maxM + nums[i] - nums[i - L])
        return res