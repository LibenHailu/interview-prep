from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                else:
                    min_min = 0

        # queue.append((0,0,0))

        neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, min_min = queue.popleft()

            for neighbour in neighbours:
                new_row = neighbour[0] + row
                new_col = neighbour[1] + col

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col, min_min + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return min_min
