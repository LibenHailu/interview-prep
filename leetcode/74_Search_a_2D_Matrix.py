class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = matrix[0][0]
        right = matrix[len(matrix) - 1][len(matrix[0]) - 1]

        while left <= right:

            mid = left + (right - left)//2

            if nums[mid] == target:
                return True

            if matrix[mid] > target:
                left = mid+1
            else:
                right = mid - 1

        return False
