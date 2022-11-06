# import sys


a,b = map(int,input().split())

# def rec(a):
#     # print(a)
#     if a > b:
#         return sys.maxsize
#     if a == b:
#         return 1
    
#     return min(1 + rec(a*2) , 1 + rec((a*10)+1))

# ifrec(a)

# try bfs

from collections import deque


queue = deque([(a,[a])])
res = []
while queue:
    a,cur =  queue.popleft()
    if a == b:
        res = cur
        break
    if a*2 <= b:
        queue.append((a*2,cur + [a*2]))
    if (a * 10) +1 <= b:
        queue.append(((a * 10) +1,cur + [(a * 10) +1]))
if res:
    print("YES")
    print(len(res))
    print(*res)
else:
    print("NO")