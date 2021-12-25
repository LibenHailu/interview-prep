class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        length=len(nums)
        for i in range(1,length):
            nums[i]+=nums[i-1]
        nums.insert(0,0)
        result=length+1
        stack=[]
        for i,n in enumerate(nums):
            while len(stack)>0 and n<=nums[stack[-1]]:
                stack.pop()
            while len(stack)>0 and n-nums[stack[0]]>=k:
                result=min(result,i-stack.pop(0))
            stack.append(i)    
        return result if result!=length+1 else -1