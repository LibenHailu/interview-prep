class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        i = 0
        count = 1
        while len(arr) > 1:
            if count == k:
                arr.pop(i)
                count = 1
            else:
                count += 1
                i += 1
                i = i % len(arr)

        return arr[0]
