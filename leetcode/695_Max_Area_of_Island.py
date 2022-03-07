class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = set()

        self.size = 0

        def inBound(row, col): return 0 <= row < len(
            grid) and 0 <= col < len(grid[0])

        def dfs(i, j):
            cur_size = 0
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            if (i, j) not in visited:
                stack = [(i, j)]

                while stack:
                    node = stack.pop()

                    if grid[node[0]][node[1]] and node not in visited:
                        visited.add(node)
                        cur_size += 1

                    for dir in directions:
                        new_row = node[0] + dir[0]
                        new_col = node[1] + dir[1]

                        if inBound(new_row, new_col) and grid[new_row][new_col] and (new_row, new_col) not in visited:
                            stack.append((new_row, new_col))

            self.size = max(self.size, cur_size)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)

        return self.size
