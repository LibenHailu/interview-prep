s = input()

def isPalindrome(t):
    return t == t[::-1]

res = ""
def pick(i,c):
    global res
    if i >= len(s):
        return ""
    if isPalindrome(c):
        res = max(res,c)
    
    if i < len(s) - 1:
        pick(i + 1,c + s[i + 1])
        pick(i + 1,c)
    


for i in range(len(s)):
    pick(i,s[i])

print(res)