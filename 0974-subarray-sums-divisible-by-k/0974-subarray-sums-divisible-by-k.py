class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = Counter()
        running_sum = 0
        res = 0
        for num in nums:
            running_sum += num
            ### 974. Subarray Sums Divisible by K
            if running_sum % k == 0: res += 1 # instead of *magic* counts[0] = 1
            res += counts[running_sum % k]
            counts[running_sum % k] += 1

            ### 560. Subarray Sum Equals K
            # if running_sum - k == 0: res += 1 # instead of *magic* counts[0] = 1
            # res += counts[running_sum - k]
            # counts[running_sum] += 1
        return res