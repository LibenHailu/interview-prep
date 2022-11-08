class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        right = xor & -xor
        res = 0
        for num in nums:
            if num & right != 0:
                res ^= num
            
        return [res,xor ^ res]
        