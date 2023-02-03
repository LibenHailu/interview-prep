class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        
        def checkPalindrome(start,end,canChange):
            if start == end or start > end:
                return True
            elif s[start] != s[end] and not canChange:
                return False
            elif s[start] != s[end] and canChange:
                return (checkPalindrome(start + 1,end,not canChange) or
                checkPalindrome(start,end - 1,not canChange))
            else:
                return checkPalindrome(start + 1 ,end - 1,canChange)
        return checkPalindrome(0,len(s) - 1, True) 
