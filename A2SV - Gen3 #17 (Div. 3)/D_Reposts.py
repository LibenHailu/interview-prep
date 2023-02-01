from collections import defaultdict


n = int(input())
graph = defaultdict(list)
nodes = []
for _ in range(n):
    s = input().split(" ")
    # print(s)
    nodes.append(s[0].lower())
    nodes.append(s[-1].lower())
    graph[s[0].lower()].append(s[-1].lower())
    # graph[s[-1].lower()].append(s[0].lower())

def dfs(node):
    visited = set()
    visited.add(node)
    stack = [(node,1)]
    ans = 1
    while stack:
        node,l = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                ans = max(ans,l+1)
                stack.append((neighbor,l+1))
    return ans
res = 0
for node in nodes:
    # if node not in visited:
    res = max(res,dfs(node)) 
print(res)
