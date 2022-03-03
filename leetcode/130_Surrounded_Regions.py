class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
#         breaks if board is empty
        def in_bound(r, c): return 0 <= r < len(
            board) and 0 <= c < len(board[0])

        DIR = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        stack = [(1, 1)]

        while stack:

            r, c = stack.pop()

            if board[r][c] == 'O':
                board[r][c] = 'X'

            for bound in DIR:
                newr = r + bound[0]
                newc = c + bound[1]

                if in_bound(newr, newc):
                    stack.append((newr, newc))

        return board
