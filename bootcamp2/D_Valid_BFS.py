from collections import defaultdict

nodes = int(input())
graph = defaultdict(set)

# building graph 
for i in range(nodes - 1):
    s,e = map(int,input().split())
    graph[s].add(e)
    graph[e].add(s)

nums = list(map(int,input().split()))

if nums[0] != 1:
    print("No")
    exit()

i,j = 0,1

while i < nodes  and j < nodes:
    if nums[j] in graph[nums[i]]:
        j += 1
    else:
        i += 1
if j == nodes:
    print("Yes")
else:
    print("No")


