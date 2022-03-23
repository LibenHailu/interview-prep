from curses import curs_set
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [1 for _ in range(len(arr))]
        max_num = 1
        flag = 1
        for i in range(len(arr)-1):
            if i % 2 == 1 and arr[i] > arr[i+1] or i % 2 == 0 and arr[i] < arr[i+1]:
                if not flag:
                    dp[i] = 1
                dp[i+1] = dp[i]+1
                max_num = max(max_num, dp[i+1])
                flag = 1
            elif i % 2 == 0 and arr[i] > arr[i+1] or i % 2 == 1 and arr[i] < arr[i+1]:
                if flag:
                    dp[i] = 1
                dp[i+1] = dp[i]+1
                max_num = max(max_num, dp[i+1])
                flag = 0
        print(dp)
        return max_num


sol = Solution()
print(sol.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))
print(sol.maxTurbulenceSize([0, 1, 1, 0, 1, 0, 1, 1, 0, 0]))
