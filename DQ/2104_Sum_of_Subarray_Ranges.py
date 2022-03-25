import math
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        gl = [None] * len(nums)
        gr = [None] * len(nums)
        ll = [None] * len(nums)
        lr = [None] * len(nums)

        s = [(0, math.inf)]

        print(s)
        for i in range(len(nums)):
            while len(s) != 0 and s[-1][-1] < nums[i]:
                s.pop()
            s.append((i+1, nums[i]))
            gl[i] = s[-1][0] - s[-2][0]

        s = [(len(nums), math.inf)]
        for i in range(len(nums)-1, -1, -1):
            while len(s) != 0 and s[-1][-1] <= nums[i]:
                s.pop()
            s.append((i, nums[i]))
            gr[i] = s[-2][0] - s[-1][0]

        s = [(0, -math.inf)]
        for i in range(len(nums)):
            while len(s) != 0 and s[-1][-1] > nums[i]:
                s.pop()
            s.append((i+1, nums[i]))
            ll[i] = s[-1][0] - s[-2][0]

        s = [(len(nums), -math.inf)]
        for i in range(len(nums)-1, -1, -1):
            while len(s) != 0 and s[-1][-1] >= nums[i]:
                s.pop()
            s.append((i, nums[i]))
            lr[i] = s[-2][0] - s[-1][0]

        g = [gl[i]*gr[i] for i in range(len(nums))]
        l = [ll[i]*lr[i] for i in range(len(nums))]

        return sum([(g[i]-l[i])*nums[i] for i in range(len(nums))])
