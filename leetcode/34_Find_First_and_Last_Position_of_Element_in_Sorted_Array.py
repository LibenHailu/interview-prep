class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        first = self.findPostition(nums, target, True)

        if first == -1:
            return [-1, -1]

        second = self.findPostition(nums, target, False)
        return [first, second]

        return [self.SearchLeft(nums, target),
                self.SearchRight(target, nums)]

    def findPostition(self, nums: List[int], target: int, isFirst: bool):
        best = -1

        left = 0
        right = len(nums)-1

        while left <= right:

            mid = (left + right)//2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            else:
                if isFirst:
                    right = mid - 1
                    best = mid
                else:
                    left = mid + 1
                    best = mid

        return best
