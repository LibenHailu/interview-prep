class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        ans = num
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    curr = nums
                    curr[i],curr[j] = curr[j],curr[i]
                    currInt = int("".join(curr))
                    ans = max(ans,currInt)
                    curr[j],curr[i] = curr[i],curr[j]
        return ans
    
