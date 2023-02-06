import bisect


n = int(input())
x = list(map(int,input().split()))
q  = int(input())
x.sort()
for _ in range(q):
    m = int(input())
    index = bisect.bisect_right(x,m)
    print(index)