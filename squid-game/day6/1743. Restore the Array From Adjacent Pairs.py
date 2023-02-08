class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visited = set()
        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        start = None
        for key,val in graph.items():
            if len(val) == 1:
                start = key
                visited.add(start)
                break
        original = []
        queue = deque([start])
        while queue:
            node = queue.popleft()
            original.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return original
        
        
