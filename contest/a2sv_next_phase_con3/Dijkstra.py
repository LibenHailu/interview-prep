
from collections import defaultdict
import heapq


def solution(dest,paths):
    neighbours = defaultdict(list)
    for path in paths:
        neighbours[path[0]].append((path[1],path[2]))
    minHeap = [(0, 1, [1])]
    
    visited = set()
    while minHeap:
        w,n, p = heapq.heappop(minHeap)
        if n == dest:
            return p
        if n in visited:
            continue

        visited.add(n)

        for new_node, new_weight in neighbours[n]:
            if new_node not in visited:
                heapq.heappush(minHeap, (w + new_weight, new_node, p + [new_node]))
             
    return [-1]
if __name__ == "__main__":
    q = list(map(int, input().rstrip().split()))
    paths = []
    for _ in range(q[1]):
        paths.append(list(map(int, input().rstrip().split())))
    res = solution(q[0],paths)
    print(*res)
