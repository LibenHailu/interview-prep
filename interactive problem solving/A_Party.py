


def solution(nodes,bosses):

    adj = {}
    for i,x in enumerate(bosses):
        adj[i + 1] = x
    # visited = set()
    res = 0
    def dfs(node,count,visited):
        nonlocal res
        res = max(res,count)
        if node in visited:
            return
        if adj[node] == -1:
            res = max(res,1)
            visited.add(node)
            return
        visited.add(node)
        dfs(adj[node],count + 1,visited)
    
    for i in range(1,nodes+1):
        dfs(i,1,set())
    print(res)

if __name__ == "__main__":
    q = int(input())
    arg = []
    for _ in range(q):
        arg.append(int(input()))
    solution(q,arg)
# solution(5,[-1,1,2,1,-1])