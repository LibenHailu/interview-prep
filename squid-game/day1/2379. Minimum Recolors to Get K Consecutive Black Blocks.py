class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = sys.maxsize
        for i in range(len(blocks) - k + 1):
            count = blocks.count('B',i,i + k)
            if count >= k:
                return 0
            ans = min(k - count,ans)
        return ans

                

