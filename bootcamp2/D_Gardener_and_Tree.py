from collections import defaultdict, deque

for t in range(int(input())):
    input()
    n,k = map(int,input().split())


    graph = defaultdict(list)
    visited = set()
    degree = [0] * n
    for _ in range(n-1):
        s,e = map(int,input().split())
        degree[s-1] += 1
        graph[e].append(s)
        degree[e-1] += 1
        graph[s].append(e)

    if k >= n:
        print(0)
        continue

    todo = deque([])
    for index,count in enumerate(degree):
        if count == 1:
            todo.append(index+1)
            degree[index] -= 1

    while todo and k:
        for _ in range(len(todo)):
            node = todo.popleft()
            n -= 1
            for neighbour in graph[node]:
        
                degree[neighbour - 1] -= 1
                if degree[neighbour - 1]  == 1:  
                    todo.append(neighbour)
        k -= 1    
    print(n)

