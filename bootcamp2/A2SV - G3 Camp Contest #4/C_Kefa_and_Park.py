# create the graph
# dfs(node,parent,k)
from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10000)
vertexies,is_okey = map(int,input().split())
has_cat = list(map(int,input().split()))
graph = defaultdict(list)
# construct the graph
for _ in range(vertexies - 1):
    edge1,edge2 = map(int,input().split())
    graph[edge1].append(edge2)
    graph[edge2].append(edge1)

# print(graph)
visited = set()
def dfs(current,parent,okey):
    # print(is_okey,okey)
    # print(current,parent,okey)
    # if okey == 0  and  parent == graph[current][0]:
    #     return 1
    
    if okey < 0 and has_cat[parent - 1] == 1:
        return 0

    # print(graph[current])
    if len(graph[current]) == 1 and parent == graph[current][0]: 
        # print(current,parent,okey)
        return 1
        

    res = 0
    for neighbour in graph[current]:
        if neighbour not in visited:
            if has_cat[neighbour - 1] == 1:
                visited.add(neighbour)
                res += dfs(neighbour,current,okey-1)
            else:
                visited.add(neighbour)
                res += dfs(neighbour,current,is_okey)
    return res

visited.add(1)
print(dfs(1,None,is_okey - has_cat[0]))
# print(visited)



# def bfs(current,parent,okey):
    # print(is_okey,okey)
    # print(current,parent,okey)
    # if okey == 0  and  parent == graph[current][0]:
    #     return 1
    
#     q = deque([(current,parent,okey)])

#     res = 0
#     while q:
#         c,p,o = q.popleft()
#         # print(c,p,o)
#         if o < 0 and has_cat[p - 1] == 1:
#             continue

#         # print(graph[current])
#         if len(graph[c]) == 1 and p == graph[c][0]: 
#             # print(current,parent,okey)
#             res += 1

#         for neighbour in graph[c]:
#             if neighbour not in visited:
#                 if has_cat[neighbour - 1] == 1:
#                     visited.add(neighbour)
#                     q.append((neighbour,c,o-1))
#                 else:
#                     visited.add(neighbour)
#                     q.append((neighbour,c,is_okey))

#     return res
        

#     # res = 0
#     # for neighbour in graph[current]:
#     #     if neighbour not in visited:
#     #         if has_cat[neighbour - 1] == 1:
#     #             visited.add(neighbour)
#     #             res += dfs(neighbour,current,okey-1)
#     #         else:
#     #             visited.add(neighbour)
#     #             res += dfs(neighbour,current,is_okey)
#     # return res

# visited.add(1)
# print(bfs(1,None,is_okey - has_cat[0]))
# # print(visited)


