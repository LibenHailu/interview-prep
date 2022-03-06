class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()
        province = 0

        def dfs(neighbours):
            # print(neighbours)
            for city, hasConnection in enumerate(neighbours):
                if hasConnection and city not in visited:
                    visited.add(city)
                    dfs(isConnected[city])

        for city, neighbours in enumerate(isConnected):
            if city not in visited:
                province += 1
                dfs(neighbours)

        return province
