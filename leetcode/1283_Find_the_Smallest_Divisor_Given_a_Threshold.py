class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def divisorSum(divisor):
            sum = 0

            for num in nums:
                sum += math.ceil(num/divisor)

            return sum

        left = 1
        right = max(nums)

        while left < right:

            mid = left + (right - left)//2

            if divisorSum(mid) <= threshold:
                right = mid

            else:
                left = mid + 1

        return right
