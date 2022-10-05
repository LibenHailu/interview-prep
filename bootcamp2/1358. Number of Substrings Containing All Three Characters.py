class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashMap = dict()
        res = 0
        left = right = 0
        
        while right < len(s):
            hashMap[s[right]] = 1 + hashMap.get(s[right],0)
            while len(hashMap) == 3:
                hashMap[s[left]] -= 1
                if hashMap[s[left]] == 0:
                    del hashMap[s[left]]
                left += 1
                res += len(s) - right 
            
            right += 1
        return res