# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

#         visited = set()

#         self.size = 0

#         def inBound(row, col): return 0 <= row < len(
#             grid) and 0 <= col < len(grid[0])

#         def dfs(i, j):
#             cur_size = 0
#             directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#             if (i, j) not in visited:
#                 stack = [(i, j)]

#                 while stack:
#                     node = stack.pop()

#                     if grid[node[0]][node[1]] and node not in visited:
#                         visited.add(node)
#                         cur_size += 1

#                     for dir in directions:
#                         new_row = node[0] + dir[0]
#                         new_col = node[1] + dir[1]

#                         if inBound(new_row, new_col) and grid[new_row][new_col] and (new_row, new_col) not in visited:
#                             stack.append((new_row, new_col))

#             self.size = max(self.size, cur_size)

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     dfs(i, j)

#         return self.size


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        par = [i for i in range(m*n)]
        rank = [0]*(m*n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rank[i*n + j] = 1

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def valid((r, c)): return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        def find(n1):
            # while n1 != par[n1]:
            # n1 = par[n1] =  par[par[n1]]
            if n1 != par[n1]:
                return find(par[n1])

            return n1

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            # if rank[r1] > rank[r2]:
            #     par[r2] = r1

            if rank[r2] > rank[r1]:
                par[r1] = r2
                rank[r2] += rank[r1]
                rank[r1] = 0
            else:
                par[r2] = r1
                rank[r1] += rank[r2]
                rank[r2] = 0

            return True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                for d in dirs:
                    r_next = i + d[0]
                    c_next = j + d[1]

                    # print(r_next,c_next,valid((r_next,c_next)))
                    if valid((r_next, c_next)) and grid[r_next][c_next] == 1:
                        n1 = i*n + j
                        n2 = r_next*n + c_next
                        union(n1, n2)
                        # print(par,n1,n2)
                        # print("########")

#         # print(m,n)
#         count = defaultdict(int)

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     continue

#                 ind = i*n +j

#                 count[find(ind)] += 1
        return max(rank)
        # print(count)
        # print(par)
        # print(rank)
        # return max(count.values() + [0])
