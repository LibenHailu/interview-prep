class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def backtrack(p,i):
            if len(p) == len(s):
                res.append(p)
                return
            if s[i].swapcase() != s[i]:
                backtrack(p+s[i].swapcase(),i + 1)
            backtrack(p+s[i],i + 1)
        backtrack("",0)
        
        return res