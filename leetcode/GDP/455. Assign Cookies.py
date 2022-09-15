class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        res = 0
        for s in s:
            if i < len(g) and s >= g[i]:
                res += 1
                i += 1
            
        return res
        