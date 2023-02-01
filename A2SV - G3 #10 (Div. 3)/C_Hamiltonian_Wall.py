def dfs(i,j,visited):
    if i == 0 and (i + 1,j) not in visited and mat[i+1][j] == "B":
        visited.add((i + 1,j))
        dfs(i+1,j,visited)
    if i == 1 and (i - 1,j) not in visited and mat[i-1][j] == "B":
        visited.add((i - 1,j))
        dfs(i - 1,j,visited)
    if j + 1 < c and (i,j + 1) not in visited and mat[i][j + 1] == "B":
        visited.add((i,j + 1))
        dfs(i ,j + 1,visited)
    if j - 1 >= 0 and (i,j - 1) not in visited and mat[i][j + 1] == "B":
        visited.add((i,j + 1))
        dfs(i ,j + 1,visited)
for _ in range(int(input())):
    c = int(input())
    mat = []
    mat.append(input())
    mat.append(input())

    