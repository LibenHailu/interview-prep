class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        l,r = 0,len(piles)-1
        while l < r:
            new_nums = [piles[l],piles[r],piles[r-1]]
            new_nums.sort()
            sum += new_nums[1]
            l += 1
            r -= 2
            
        return sum
        