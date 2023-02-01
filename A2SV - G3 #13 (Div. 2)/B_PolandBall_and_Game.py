import math


n,m = map(int,input().split())
set1 = set()
set2 = set()
for i in range(n):
    set1.add(input())

for j in range(m):
    set2.add(input())

i = len(set1.intersection(set2))
if i % 2 == 0:
    if n - i > m - i:
        print("YES")
    else:
        print("NO")
else:
    if n - i // 2 > m - math.ceil(i / 2):
        print("YES")
    else:
        print("NO")