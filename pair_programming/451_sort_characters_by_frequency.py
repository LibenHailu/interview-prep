import collections
import heapq


class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        print(count)
        h = []

        for word, fre in count.items():

            heapq.heappush(h, (fre, word))
        res = []
        for i in range(len(h)):
            f, w = heapq.heappop(h)
            res.append(w*f)
        return ''.join(res)[::-1]


sol = Solution()
print(sol.frequencySort("Aabb"))
