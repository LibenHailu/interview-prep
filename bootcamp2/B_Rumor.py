
from curses import KEY_UNDO
from inspect import stack
from operator import ne
import sys


n,r = map(int,input().split())
cost = list(map(int,input().split()))
neighbours = {}
for _ in range(r):
    k,v = map(int,input().split())
    neighbours[k] = v

visited = set()
res = 0
for key in neighbours:
    min_cost = sys.maxsize
    # print(min_cost)
    if key not in visited:
        stack = [key]
        visited.add(key - 1)
        while stack:
            node = stack.pop()
            min_cost =  min(min_cost,cost[node-1])
            # print(min_cost)
            if neighbours[node] in neighbours and  neighbours[node]-1  not in visited:
                stack.append(neighbours[node])
                visited.add(neighbours[node] - 1)
        print(min_cost)
        res += min_cost

for i in range(len(cost)):
    if i not in visited:
        res+= cost[i]
print(res)
