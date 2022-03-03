class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        left = 1
        right = m * n

        while left < right:
            mid = left + (right - left) // 2

            if self.count(m, n, mid) < k:
                left = mid + 1
            else:
                right = mid

        return left

    def count(self, m: int, n: int, mid: int):

        count = 0

        for row in range(1, m+1):
            count += min(mid/row, n)

        return count
