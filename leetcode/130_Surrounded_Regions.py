class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inBound(row, col): return 0 <= row < len(
            board) and 0 <= col < len(board[0])

        def surounded(i, j):
            visited = set()
            stack = [(i, j)]

            visited.add((i, j))

            while stack:
                node = stack.pop()

                for direction in directions:
                    new_row = node[0] + direction[0]
                    new_col = node[1] + direction[1]

                    if new_row < 1 or new_col < 1 or new_row > len(board) - 2 or new_col > len(board[0]) - 2:
                        if inBound(new_row, new_col) and board[new_row][new_col] == "O":
                            return False

                    if inBound(new_row, new_col) and board[new_row][new_col] == "O" and (new_row, new_col) not in visited:
                        stack.append((new_row, new_col))
                        visited.add((new_row, new_col))

            return True

        def mark(i, j):
            visited = set()
            stack = [(i, j)]

            visited.add((i, j))

            while stack:
                node = stack.pop()

                board[node[0]][node[1]] = "X"

                for direction in directions:
                    new_row = node[0] + direction[0]
                    new_col = node[1] + direction[1]
                    if board[new_row][new_col] == "O" and (new_row, new_col) not in visited:
                        stack.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "O":
                    isSurounded = surounded(i, j)

                    if isSurounded:

                        mark(i, j)

        return board
