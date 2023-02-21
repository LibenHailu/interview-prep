class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0]*n
        for start,end in edges:
            indegrees[end] += 1

        return [i for i in range(n) if indegrees[i] == 0]
         
