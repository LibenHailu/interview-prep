
def dfs(x,y,x1,y1):
	v.add((x,y))
	for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
		if x+dx>=0 and x+dx<n and y+dy>=0 and y+dy<m and (x+dx,y+dy)!=(x1,y1) and a[x+dx][y+dy]==a[x][y]:
			if (x+dx,y+dy) in v or dfs(x+dx,y+dy,x,y):
				return True
	return False
import sys
sys.setrecursionlimit(10000)
n,m=map(int,input().split())
a=[input() for i in range(n)]
v=set()
for i in range(n):
	for j in range(m):
		if not (i,j) in v and dfs(i,j,-1,-1):
			print('Yes')
			quit()
print('No')