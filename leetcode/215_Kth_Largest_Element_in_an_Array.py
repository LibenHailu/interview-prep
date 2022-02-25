class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        h = []

        for i in nums:
            heapq.heappush(h, -i)

        while k <= len(nums) and k > 1:
            heapq.heappop(h)
            k -= 1

        return -heapq.heappop(h)
