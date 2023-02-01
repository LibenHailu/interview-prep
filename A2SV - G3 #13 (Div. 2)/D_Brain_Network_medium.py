from collections import defaultdict
 
 
n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
 
ans = 0
visited = set()
def dfs(n):
    global ans,visited
    # visited = set()
    stack = [(n,0)]
    visited.add(n)
    # cur = 0
    while stack:
        n,d = stack.pop()       
        ans = max(ans,d)
 
        for neigh in graph[n]:
            if neigh not in visited:
                visited.add(neigh)
                stack.append((neigh,d+1))
 
for key in graph:
    if len(graph[key]) == 1 and key not in visited:
        dfs(key)
# for i in range(1,n+1):
# n(n+m)
print(ans)