class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        self.ans = 0

        visited = set()

        def inBound(row, col): return 0 <= row < len(
            grid) and 0 <= col < len(grid[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j):

            stack = [((i, j))]
            count = 1
            visited.add((i, j))
            surrounded = True

            while stack:
                node = stack.pop()

                for direction in directions:
                    new_row = node[0] + direction[0]
                    new_col = node[1] + direction[1]

                    if new_row < 1 or new_col < 1 or new_row > len(grid) - 2 or new_col > len(grid[0]) - 2:
                        if inBound(new_row, new_col) and grid[new_row][new_col] == 1:
                            surrounded = False

                    if inBound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        stack.append((new_row, new_col))
                        count += 1
                        visited.add((new_row, new_col))

            if surrounded:
                return count
            return 0

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):

                if (i, j) not in visited and grid[i][j] == 1:
                    count = dfs(i, j)
                    self.ans += count

        return self.ans
