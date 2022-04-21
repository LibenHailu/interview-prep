class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        par = [i for i in range(m*n)]
        rank = [1]*m*n

        def find(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]

            return n1

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            if rank[r1] > rank[r2]:
                par[r2] = r1

            elif rank[r2] > rank[r1]:
                par[r1] = r2

            else:
                par[n1] = r2
                rank[r1] += 1
#
            return True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):

                if grid[i][j] == "0":
                    continue
                for direction in directions:
                    x_next, y_next = i+direction[0], j+direction[1]
                    if 0 <= x_next < m and 0 <= y_next < n and grid[x_next][y_next] == "1":
                        cur_node_idx = i*n+j
                        nei_node_idx = x_next*n + y_next
                        union(cur_node_idx, nei_node_idx)

        count = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                cur_node_idx = i*n+j
                root_node = find(cur_node_idx)
                count[root_node] += 1

        return len(count)
