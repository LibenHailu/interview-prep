class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)
        for i,route in enumerate(routes):
            for j in route:
                graph[j].add(i)
        
        queue = deque([(source,0)])
        visited = set([source])
        seen = set()
        while queue:
            node,buses = queue.popleft()
            if node == target:
                return buses
            
            for i in graph[node]:
                for j in routes[i]:
                    if j not in visited:
                        visited.add(j)
                        queue.append((j,buses + 1))
                routes[i] = []
                
        return -1
