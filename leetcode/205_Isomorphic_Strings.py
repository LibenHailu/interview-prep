class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = t[i]
            else:
                if hashMap[s[i]] != t[i]:
                    return False

        return True
