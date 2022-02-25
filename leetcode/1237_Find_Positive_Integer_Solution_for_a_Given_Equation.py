"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:

        arr, right = [], z+1

        for i in range(1, z+1):

            if customfunction.f(i, 1) > z:

                return arr

            left = 1

            while customfunction.f(i, right-1) > z:

                mid = (left + right) // 2

                if customfunction.f(i, mid) > z:
                    right = mid
                else:
                    left = mid

            if customfunction.f(i, right - 1) == z:
                right -= 1
                arr.append([i, right])

        return arr
