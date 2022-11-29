from collections import defaultdict
import sys


for _ in range(int(input())):
    n = input()
    l = r = 0
    s = defaultdict(int)
    s[n[0]] = 1
    res = sys.maxsize
    while r < len(n):
        if len(s) < 3:
            r += 1
            if r < len(n):
                s[n[r]] += 1
        else:
            res = min(res,(r - l) + 1)
            s[n[l]] -= 1
            if s[n[l]] == 0:
                del s[n[l]]
            l += 1
            

    print(res if res != sys.maxsize else 0)
