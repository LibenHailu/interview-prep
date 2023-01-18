class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = - sys.maxsize 
        max_ending_here = 0
        for i in range(len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            
            if(max_ending_here < 0):
                max_ending_here = 0
        return max_so_far
# 
    # def maxCrossingSum(self,nums,l,m,h):
#         sm = 0
#         left_sum = -sys.maxsize
#         for i in range(m,l - 1, -1):
#             sm += nums[i]
#             if sm > left_sum:
#                 left_sum = sm
#         sm = 0
#         right_sum = -sys.maxsize
#         for j in range(m,h+1):
#             sm += nums[j]
#             if sm > right_sum:
#                 right_sum = sm
        
#         return max(left_sum + right_sum - nums[m],left_sum,right_sum)
    
#     def maxSubArraySum(self,nums,l,h):
#         if l > h:
#             return -sys.maxsize
#         if l == h:
#             return nums[l]
#         m = (l + h) // 2
#         left_sum = self.maxSubArraySum(nums,l,m - 1)
#         right_sum = self.maxSubArraySum(nums,m + 1, h)
#         cross_sum = self.maxCrossingSum(nums,l,m,h)
        
#         return max(left_sum,right_sum,cross_sum)
        
            # return self.maxSubArraySum(nums,0,len(nums) - 1)
        
        