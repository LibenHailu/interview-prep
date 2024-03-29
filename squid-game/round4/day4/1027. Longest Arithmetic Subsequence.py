class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i in xrange(len(A)):
            for j in xrange(i + 1, len(A)):
                dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
        return max(dp.values())