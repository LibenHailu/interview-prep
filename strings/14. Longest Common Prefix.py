class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort(key=len)
        x = strs[0]
        i = 1
        while i < len(strs):
            if strs[i].startswith(x):
                i += 1
            else:
                x = x[:-1]
        
        return x