
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        # if x == self.root[x]:
        #     return x
        # self.root[x] = self.find(self.root[x])
        # return self.root[x]
        while  x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]
            # else:
            #     self.root[rootY] = rootX
            #     self.rank[rootX] += 1
# from collections import defaultdict
# from functools import lru_cache
# from os import name
# import sys
# import threading

# visited = set()
# graph = defaultdict(list)
# def dfs(i):
#     stack = [i]
#     res = 0
#     while stack:
#         node = stack.pop()
#         res += 1
#         for neghbour in graph[node]:
#             if neghbour not in visited:
#                 visited.add(neghbour)
#                 stack.append(neghbour)
#     return res
# def dfs(i):
#     res = 1
#     for neghbour in graph[i]:
#         if neghbour not in visited:
#             visited.add(neghbour)
#             res += dfs(neghbour)

#     return res

n,m = map(int,input().split())


uf = UnionFind(n + 1)
# def main():
for i in range(m):
    group = list(map(int,input().split()))
    if len(group) < 2:
        continue
    for i in range(2,len(group)):
        # uf.union(group[1]u,group[i])
        uf.union(group[i],group[i - 1])
#         graph[group[i - 1]].append(group[i])
#         graph[group[i]].append(group[i - 1])

# res = []
# for i in range(1,n+1):
#     visited.add(i)
#     res.append(dfs(i))
#     visited = set()
# print(*res)


# if name == "__main__":
#     threading.stack_size(1 << 27)
#     sys.setrecursionlimit(1 << 30)
#     main_thread = threading.Thread(target=dfs)
#     main_thread.start()
#     main_thread.join()
res = []
for i in uf.root:
    if i == 0:
        continue
    res.append(uf.rank[uf.find(i)])
print(*res)
# print(*[uf.rank[uf.find(i)] for i in range(1,n + 1)])
