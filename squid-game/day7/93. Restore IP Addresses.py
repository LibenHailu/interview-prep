class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(i,curr):
            if i >= len(s):
                if "".join(curr) == s and len(curr) == 4:
                    res.append(".".join(curr))
            
            if i < len(s):
                backtrack(i+1,curr + [s[i]])
                
            if i + 1 < len(s) and s[i] != "0":
                backtrack(i + 2,curr + [s[i: i + 2]])
                
            if i + 2 < len(s) and s[i] != "0" and int(s[i : i+3]) <= 255:
                backtrack(i + 3,curr + [s[i : i+3]])
                
        backtrack(0,[])
        backtrack(1,[])
        backtrack(2,[])
    
        return res