class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        f = [0] * n
        f[0] = 1
        f[1] = 1

        for i in range(2, n):
            f[i] = f[i-1] + f[i-2]

        return f[n-1]
