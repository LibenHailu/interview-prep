class Solution:
    def __init__(self):
        self.dict = {}
    
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n in self.dict:
            return self.dict[n]
        ans = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.dict[n] = ans
        return ans
        # return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
    
    