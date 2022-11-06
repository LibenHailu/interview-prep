from collections import defaultdict

length,k = map(int,input().split())
present = input()
l = 0
hash = {"a":0,"b":0}
ans = 0

for r in range(length):
    
    hash[present[r]] += 1
    while min(hash.values()) > k:
        hash[present[l]] -= 1
        l += 1
    ans = max(ans,r - l + 1)

print(ans)