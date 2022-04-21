class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        edges = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[j][0] - points[i][0]) + \
                    abs(points[j][1] - points[i][1])
                edges.append((dist, i, j))

        edges.sort()

        pars = [i for i in range(len(points))]
        ranks = [1]*len(points)

        def find(n):
            while n != pars[n]:
                pars[n] = pars[pars[n]]
                n = pars[n]
            return n

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            if r2 > r1:
                pars[r1] = r2
                ranks[r2] += ranks[r1]
                ranks[r1] = 0
            else:
                pars[r2] = r1
                ranks[r1] += ranks[r2]
                ranks[r2] = 0

            return True

        answer = 0
        for edge in edges:

            if union(edge[1], edge[2]):
                answer += edge[0]

        return answer
