
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_idx = 0
        for idx, num in enumerate(citations):
            if num >= idx + 1:
                h_idx = idx + 1
            else:
                break

        return h_idx
