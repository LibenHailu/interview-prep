import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        h = []
        res = []

        for key, value in count.items():
            heapq.heappush(h, (-1*value, key))

        while k > 0:
            _, val = heapq.heappop(h)
            res.append(val)
            k -= 1

        return res
