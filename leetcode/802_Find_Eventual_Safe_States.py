class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        ingoing = defaultdict(list)
        inDegrees = [0]*len(graph)
        result = []

        for index, edge in enumerate(graph):
            inDegrees[index] = len(edge)
            for value in edge:
                ingoing[value].append(index)

        queue = deque()
        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                queue.append(i)

        while queue:
            safe = queue.pop()
            result.append(safe)

            for neighbor in ingoing[safe]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)

        result.sort()
        return result
