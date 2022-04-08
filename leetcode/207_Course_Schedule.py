class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        inDegrees = [0]*numCourses
        outgoing = defaultdict(set)

        for course, pre in prerequisites:
            outgoing[pre].add(course)
            inDegrees[course] += 1

        queue = deque()
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)

        count = 0
        while queue:
            course = queue.popleft()
            count += 1
            for neighbor in outgoing[course]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)

        return count == numCourses
