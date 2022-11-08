class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = len(nums) + 1
        pre = [0]
        
        for num in nums:
            pre.append(pre[-1] + num)
        
        monoq = deque()
        for ind,val in enumerate(pre):
            # y -x >= k
            while monoq and val <= pre[monoq[-1]]:
                monoq.pop()
            
            while monoq and val - pre[monoq[0]] >= k:
                ans = min(ans,ind - monoq.popleft())
            
            monoq.append(ind)
        
        return ans if ans < len(nums) + 1 else -1
            