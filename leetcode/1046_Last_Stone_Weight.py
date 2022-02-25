class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        h = []
        for i in stones:
            heapq.heappush(h, -i)

        while len(h) >= 2:
            y = -1 * heapq.heappop(h)
            x = -1 * heapq.heappop(h)

            if y > x:
                heapq.heappush(h, -1*(y-x))

        return -1*heapq.heappop(h) if h else 0
