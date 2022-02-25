class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []

        for list in matrix:
            h.extend(list)

        heapq.heapify(h)

        while len(h) >= k and k > 1:
            heapq.heappop(h)
            k -= 1

        return heapq.heappop(h)
