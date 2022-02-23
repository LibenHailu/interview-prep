class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        result = []
        heap = []

        for key, value in count.items():
            heapq.heappush(heap, (-1*value, key))

        while k > 0:
            _, key = heapq.heappop(heap)
            result.append(key)
            k -= 1

        return result
