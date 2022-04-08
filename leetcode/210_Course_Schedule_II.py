class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        inDegrees = [0] * numCourses
        outgoing = defaultdict(set)
        result = []

        for course, prerequisite in prerequisites:
            outgoing[prerequisite].add(course)
            inDegrees[course] += 1

        queue = deque()
        for i in range(len(inDegrees)):
            if inDegrees[i] == 0:
                queue.append(i)

        count = 0
        while queue:

            course = queue.popleft()
            result.append(course)
            count += 1

            for neighbor in outgoing[course]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)

        return result if count == numCourses else []
