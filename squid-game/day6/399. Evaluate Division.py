class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)
        ans = []
        for i,(u,v) in enumerate(equations):
            graph[u] += [[v,values[i]]]
            graph[v] += [[u,1/values[i]]]
        
      
        def compute(s,e):
            queue = deque([[s,1]])
            visited = set()
            while queue:
                nextqueue = deque()
                for [node,w] in queue:
                    if node == e and e in graph:
                         return w
                    visited.add(node)
                    for [neig,weig] in graph[node]:
                        if neig not in visited:
                            nextqueue.append([neig,weig*w])
                queue = nextqueue
            return float(-1)
        
        for (start,end) in queries:
            ans.append(compute(start,end))
        
        return ans