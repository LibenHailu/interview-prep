# from collections import defaultdict
# import heapq
# import sys


for _ in range(int(input())):
    n,m = map(int,input().split())
    ans = 0
    if n == 1:
        print(sum(i for i in range(1,m+1)))
        continue
    if m == 1:
        print(sum(i for i in range(1,n+1)))
        continue
    ans = 0
    for x in range(1,m):
        ans += x
    # print(ans)
    for x in range(1,n + 1):
        # print((x - 1)*m  + m)
        ans += (x - 1)*m  + m
    # ans -= (1 - 1)*m  + m
    print(ans)

#     # mat = [[0] * m  for _ in range(n)]
#     # path = [[sys.maxsize] * m  for _ in range(n)]
#     path = defaultdict(lambda: sys.maxsize)
#     # for i in range(1,len(mat)+ 1):
#     #     for j in range(1,len(mat[0]) + 1):
#     #         mat[i-1][j-1] = 100000 + (i - 1)*m  + j
#     # mat[0][0] -= 100000
#     heap = [((1 - 1)*m  + 1,0,0)]
#     path[(0,0)] = (1 - 1)*m  + 1
#     DIRS = [(0,1),(1,0)]
#     inbound = lambda r,c: 0 <= r  < n and 0 <= c  < m
#     while heap:
#         p,i,j = heapq.heappop(heap)
#         if i == n - 1 and j == m -1:
#             print(p)
#             break
        
#         for r,c in DIRS:
#             next_r,next_c = i + r,j + c
#             dest = p + ((next_r + 1) - 1)*m  + (next_c + 1)
#             if inbound(next_r,next_c) and dest < path[(next_r,next_c)]:
#                 path[(next_r,next_c)] = dest
#                 heapq.heappush(heap,(dest,next_r,next_c))
        
