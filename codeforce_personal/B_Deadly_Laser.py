# start form the end index
# walk through top
for _ in range(int(input())):
    n, m, sx, sy, d = map(int, input().split())
    
    if min(sx - 1, m - sy) <= d and min(n - sx, sy - 1) <= d:
	    print(-1)
    
    else:
        print(n + m - 2)
