from collections import defaultdict


n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(input()))
crossed = defaultdict(list)
for row in range(n):
    for col in range(m):
        
        for c in grid[row]:
            crossed[(row,col)].append(c)
        
        for j in range(n):
            if j != row:
                crossed[(row,col)].append(grid[j][col])
ans = []
for i in range(n):
    for j in range(m):
        if crossed[(i,j)].count(grid[i][j]) == 1:
            ans.append(grid[i][j])  
print("".join(ans))