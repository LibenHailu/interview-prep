class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if not n > 1:
            return ""

        for char in range(((n-1)//2)+1):
            if not palindrome[char] == "a":
                print(palindrome[char])
                if (not n % 2 == 0) and (char == (n-1)//2):
                    break
                palindrome = palindrome[0:char] + "a" + palindrome[char+1:n]
                return palindrome

        palindrome = palindrome[0:n-1] + "b"
        return palindrome
