import sys


def solve(s,k):
    change = 0
    l = 0
    r = 0
    ans = sys.maxsize
    while r < len(s):

        if s[r] == "E":
            change += 1

        # if (r - l )+ 1  == k:
        #     ans = min(ans,change)
        if change < 0:
            if s[l] == "E":
                change -= 1
                l += 1
        r += 1
    
    return ans

print(solve("ETTEETTETE",7))
print(solve("ETETTTE",2))