from collections import defaultdict
from email.policy import default


l = int(input())
nums = list(map(int,input().split()))
graph = defaultdict(list)
love = "NO"

for i in range(l):
    # if i+1 not in grapgh:
    if love == "YES":
        break
    if i + 1 in graph:
        for n in graph[i + 1]:
            if nums[i] in graph[n]:
                love = "YES"
                break
    graph[i+1].append(nums[i])
    graph[nums[i]].append( i + 1)
print(love)