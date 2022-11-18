import sys

k = int(input())
input1 = input()
change = 0
l = 0
r = 0
ans = sys.maxsize
while r < len(input1):
    if input1[r] == "E": 
        change += 1
    if (r - l) + 1 == k:
        ans = min(ans,change)
        if input1[l] == "E":
            change -= 1
        l += 1
    
    r += 1

print(ans)