from collections import deque

n,m,k = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))

DIRS = [(1,0),(0,1),(-1,0),(0,-1)]

empty = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            empty += 1

queue = deque([])
has_found = False
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == ".":
            queue.append((x,y))
            grid[x][y] = "S"
            has_found = True
            break
    if has_found:
        break
# print(empty)
k = empty-k
while queue and k > 0:
    # print(queue)
    # if grid[i][j] == "S":
    #     continue
    i,j = queue.popleft()
    for r,c in DIRS:
        if 0 <= i+r < len(grid) and 0 <= j+c < len(grid[0]) and grid[i+r][j+c] == "." and k > 1:
            k -= 1
            queue.append((i+r,j+c))
            grid[i+r][j+c] = "S"

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            grid[i][j] = "X"
        if grid[i][j] == "S":
            grid[i][j] = "."
for row in grid:
    print("".join(row))