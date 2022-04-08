class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def predict(left, right, turn):

            if left == right:
                if turn == 0:
                    return nums[left]
                else:
                    return -nums[left]

            if turn == 0:
                return max(nums[left] + predict(left+1, right, 1 - turn), -nums[right] + predict(left, right-1, 1 - turn))

            if turn == 1:

                return min(-nums[left] + predict(left+1, right, 1 - turn), -nums[right] + predict(left, right-1, 1-turn))

        return predict(0, len(nums) - 1, 0) > 0


sol = Solution()
print(sol.PredictTheWinner([1, 5, 2]))
