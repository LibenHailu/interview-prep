# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:

#         visited = set()
#         province = 0

#         def dfs(neighbours):
#             # print(neighbours)
#             for city, hasConnection in enumerate(neighbours):
#                 if hasConnection and city not in visited:
#                     visited.add(city)
#                     dfs(isConnected[city])

#         for city, neighbours in enumerate(isConnected):
#             if city not in visited:
#                 province += 1
#                 dfs(neighbours)

#         return province

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        edges = []

        for i in range(1, len(isConnected) + 1):
            for j in range(1, len(isConnected[0])):
                if isConnected[i-1][j-1] == 1 and i != j:
                    edges.append((i, j))

        pars = [i for i in range(1, len(isConnected) + 1)]
        ranks = [1]*len(isConnected)

        def find(n1):
            # while n1 != pars[n1-1]:
            #     n1 = pars[n1 - 1] = pars[pars[n1 - 1] - 1]
            # return n1
            if n1 != pars[n1 - 1]:
                pars[n1 - 1] = pars[pars[n1 - 1] - 1]
                return find(pars[n1 - 1])

            return n1

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            if ranks[r2 - 1] > ranks[r1 - 1]:
                pars[r1 - 1] = r2
                ranks[r2 - 1] += ranks[r1 - 1]
            else:
                pars[r2 - 1] = r1
                ranks[r1 - 1] += ranks[r2 - 1]

        for e in edges:
            union(e[0], e[1])

        count = collections.defaultdict(int)
        for i in range(1, len(isConnected) + 1):
            root_node = find(i)
            count[root_node] += 1

        return len(count)
