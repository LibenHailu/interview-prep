class Solution:
    def romanToInt(self, s: str) -> int:
        romanIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0

        for i in range(len(s) - 1,-1,-1):
            if i+1 < len(s) and romanIntDict[s[i]] < romanIntDict[s[i+1]]:
                ans -= romanIntDict[s[i]]
            else:
                ans += romanIntDict[s[i]]
        
        return ans