class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left, right = max(weights), sum(weights)

        while left < right:

            mid = left + (right - left) // 2
            current = 0
            myDays = 1
            for w in weights:
                if current + w > mid:
                    myDays += 1
                    current = 0
                current += w

            if myDays > days:
                left = mid + 1
            else:
                right = mid

        return left
