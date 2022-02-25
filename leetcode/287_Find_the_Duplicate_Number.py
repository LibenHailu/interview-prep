from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        left, right = 1, len(nums)-1

        # Loop is O(logn), excluding the inner-loop, total is O(nlogn)
        while left < right:

            mid = (right + left)//2

            print(mid)

            count = 0

            for i in nums:
                if i <= mid:
                    count += 1

            if count <= mid:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate([1, 3, 4, 2, 2]))
