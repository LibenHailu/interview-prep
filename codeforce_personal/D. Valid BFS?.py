from collections import defaultdict, deque


def solution(neighbours,path):
    adj = defaultdict(list)
    for neighbour in neighbours:
        adj[neighbour[0]].append(neighbour[1])
        adj[neighbour[1]].append(neighbour[0])
    
    visited = set()
    queue = deque([1])
    visited.add(1)
    pointer = 1
    while queue:
        node = queue.popleft()
        visited.add(node)
        for i in range(len(adj[node])):
            print(i,"here")
            if pointer < len(path) and path[pointer] not in visited and path[pointer] in adj[node]:
                queue.append(path[pointer])
                pointer += 1

            else:
                # print(visited,path[pointer],queue,adj[2])
                # print(pointer < len(path))
                # print(path[pointer] not in visited)
                # print(path[pointer] in adj[node])
                print(pointer)
                return "NO"
    
    return "YES"
    
    # res = []
    # while queue:
    #     print(res)
    #     node,index = queue.popleft()
    #     res.append(node)
    #     print(node,"node here")
    #     print(res)
    #     length = len(adj[node])
    #     for i in range(index+1,index+length+1):
    #         print("hey", node)
    #         if i < len(path) and path[i] not in adj[node]:
    #             print(path[i],adj[node],node)
    #             return False
    #         else:
    #             print("here")
    #             queue.append((path[i],index+1))

    # levels = {}
    # visited = set()
    # queue = deque([(1,0)])
    # visited.add(1)
    # while queue:
    #     current,level = queue.popleft()
    #     levels[current] = level

    #     for neighbour in adj[current]:
    #         if neighbour not in visited:
    #             visited.add(neighbour)
    #             queue.append((neighbour,level+1))
    # for i in range(1,len(path)):
    #     if levels[path[i - 1 ]] > levels[path[i]]:
    #         return "NO"
    # return "YES"


if __name__ == "__main__":
    q = int(input())
    neighbours = []
    for _ in range(q - 1):
        neighbours.append(list(map(int, input().split())))
    path = list(map(int, input().split()))
print(solution(neighbours,path))