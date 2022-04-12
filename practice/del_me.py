from collections import defaultdict
from typing import List


class Solution:
    def eventualSafeNodes(self, adjList: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        v = len(adjList)

        for node in range(v):
            graph[node].extend(adjList[node])

        cyclic = set()

        def detect_cycle(visited, dfs_stack, node):
            visited.add(node)
            dfs_stack.add(node)

            for adj in graph[node]:
                if adj not in visited:
                    if detect_cycle(visited, dfs_stack, adj):
                        cyclic.add(node)
                        return True

                if adj in dfs_stack:
                    cyclic.add(node)
                    return True

            dfs_stack.remove(node)
            return False

        visited, dfs_st = set(), set()
        for i in range(len(adjList)):
            if i not in visited:
                detect_cycle(visited, dfs_st, i)

        return [node for node in range(len(adjList)) if node not in cyclic]


sol = Solution()
print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
