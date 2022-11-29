from collections import defaultdict


v,e = map(int,input().split())
graph = defaultdict(list)
for i in range(e):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = set()

def dfs(node):
    has_cycle = True
    stack = [node]
    while stack:
        n = stack.pop()
        if len(graph[n]) != 2:
            has_cycle = False

        for neighbour in graph[n]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
            
    return has_cycle

ans = 0
for node in range(1, v+1):
    if node not in visited:
        visited.add(node)
        ans += dfs(node)

print(ans)