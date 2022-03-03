class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])

        # lambda function to check wheather we are inside the matrix
        def in_bound(row, col): return 0 <= row < n and 0 <= col < m

        start_color = image[sr][sc]
        image[sr][sc] = newColor
        DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        stack = [(sr, sc)]
        visited = set([(sr, sc)])

        while stack:
            cur_row, cur_col = stack.pop()
            for direction in DIR:  # iterate through negihbours
                new_row = cur_row + direction[0]
                new_col = cur_row + direction[1]

                if (new_row, new_col) in visited or not in_bound(new_row, new_col) or image[new_row][new_col] != start_color:
                    continue
                visited.add((new_row, new_col))
                image[new_row][new_col] = newColor
                stack.append((new_row, new_col))
                print(stack)

        return image
