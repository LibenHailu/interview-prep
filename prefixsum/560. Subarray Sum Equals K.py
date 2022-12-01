class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        prefsum=0
        d={0:1}
        for num in nums:
            prefsum += num
            if prefsum-k in d:
                ans += d[prefsum-k]
            if prefsum not in d:
                d[prefsum] = 1
            else:
                d[prefsum] += 1
        return ans
#         res = 0
#         curSum = 0
#         prefixSum = {0:1}
#         for num in nums:
#             curSum += num
#             if curSum - k in prefixSum:
#                 res += prefixSum[curSum - k]
#             elif curSum in prefixSum:
#                 prefixSum[curSum] += 1
#             else:
#                 prefixSum[curSum] = 1
            
        
            